from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book, Cart, Order, OrderItem




#this one renders both the normal home page and also used to fulfill the list file as well
def home(request):

#this books is now a query set or like a python object
    books = Book.objects.all()


#here i am using the query done by client and try to search books ignoring case sensetive
    query = request.GET.get('q')
    if query:
        books = books.filter(
            Q(title__icontains = query) | Q(author__icontains = query)
        )

#stock status is on fly attribute that won't be saved in database, but in memory.
    for book in books:
        if book.stock < 5:
            book.stock_status = 'Out of Stock'
        elif book.stock == 0:
            book.stock_status = 'Out of Stock'
        elif book.stock == 1:
            book.stock_status = 1  #'Low Stock 1 left'
        else:
            book.stock_status = 'In Stock'

    return render(request, 'list.html', {'books' : books, 'query_searched': query or ''})
#here the query_searched string will be used in django template as a variable







def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('confirm')
        email = request.POST.get('email')

        if password != password1:
            return render(request, 'registration.html', {'message' : 'Error, passwords are not the same'})
        
        if User.objects.filter(username = username).exists():
            return render(request, 'registration.html', {'message' : 'This username already exists'})
        
        try:
            user = User.objects.create_user(username = username, password = password, email=email)
            user.save()
            login(request, user)
            messages.success(request, username)
            return redirect('home')

        except Exception as e:
            return render(request, 'registration.html', {'message' : str(e)})
        
    return render(request, 'registration.html')

 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user:
            login(request, user)
            messages.success(request, username)
            return redirect('books:home')
        else:
            return render(request, 'login.html', {'message' : 'Login failed'})
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('books:home')

        

def about(request):
    return render(request, 'about.html')


def detail(request, id):
    book = get_object_or_404(Book, id=id)

    
    if book.stock < 5:
        book.stock_status = 'Out of Stock'
    elif book.stock == 0:
        book.stock_status = 'Out of Stock'
    elif book.stock == 1:
            book.stock_status = 'Low Stock 1 left'
    else:
        book.stock_status = 'In Stock'
        
    return render(request, 'detail.html', {'book': book})



@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Check if book is in stock
    if book.stock <= 0:
        messages.error(request, "Sorry, this book is out of stock.")
        return redirect("books:detail", id=book_id)

    # Get existing cart item or create new one
    cart_item, created = Cart.objects.get_or_create(
        user=request.user, 
        book=book,
        defaults={'quantity': 1}
    )
    
    if not created:
        # Item already exists, increase quantity
        if cart_item.quantity + 1 <= book.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Book added to cart successfully.")
        else:
            messages.warning(request, f"Sorry, only {book.stock} copies available.")
    else:
        messages.success(request, "Book added to cart successfully.")
    
    return redirect("books:cart")


@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    # Calculate stock status for each book in cart
    for item in cart_items:
        book = item.book
        if book.stock < 5:
            book.stock_status = 'Out of Stock'
        elif book.stock == 0:
            book.stock_status = 'Out of Stock'
        elif book.stock == 1:
            book.stock_status = 'Low Stock 1 left'
        else:
            book.stock_status = 'In Stock'
    
    total = sum(item.book.price * item.quantity for item in cart_items)
    return render(request, "cart.html", {"cart_items": cart_items, "total": total})


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect("books:cart")


@login_required
def update_quantity(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        
        if quantity > 0 and quantity <= cart_item.book.stock:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Cart updated successfully.")
        else:
            messages.error(request, f"Invalid quantity. Available: {cart_item.book.stock}")
    
    return redirect("books:cart")

    


def checkout(request):
    return render(request, 'checkout.html')



def orders(request):
    return render(request, 'orders.html')



def checkout(request):

    '''
    what to do?
    1. get Cart of this user from Cart model
    2. check if all informations are filled 
    3. check if the ordered quantity of each book is <= stock
    4. if everything is fine so far, then register all informations in Order and OrderItem models
    5. and then render the page with the messages.
    6. stock has to be updated.
    7. deleting the cart if the order is placed successfully
    '''
    #1
    cart_items = Cart.objects.filter(user = request.user)

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        #2
        if not all(['firstname', 'lastname', 'email', 'phone', 'address']):
            messages.error(request, 'Sorry, there is a missing information')
            return redirect('checkout')
        
        #3
        for item in cart_items:
            if item.quantity > item.book.stock:
                messages.error("sorry only " + item.book.stock + " copies of " + item.book.title + " are left")
                return redirect('checkout')
            
        #4
        order = Order.objects.create(user = request.user, shipping_address = address,
                                    total_amount = sum(item.quantity * item.book.price for item in cart_items) 
                                    ) #here we used a generator expression to calculate the total amount
        
        #5
        for item in cart_items:
            OrderItem.objects.create(
                                     quantity = item.quantity, 
                                     price = item.book.price, #this has to be for a single book price
                                     book = item.book,
                                     order = order) #this order is from #4
            
        #6
        for item in cart_items:
            item.book.stock -= item.book.stock - item.quantity
            item.book.save()

        #7
        cart_items.delete()

        messages.success(request, 'Successfully placed')
        return render(request, 'success.html')

    return render(request, 'checkout.html')
