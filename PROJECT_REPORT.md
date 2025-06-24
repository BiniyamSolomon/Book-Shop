Django Bookshop - Technical Implementation Report

1. Project Overview

Application: Django Bookshop Website ("Ciao Book Shop")
Technology: Django, Python, HTML, CSS, JavaScript, SQLite database
Type: E-commerce website for selling books online
Development: Complete working bookshop with all basic features

2. What Has Been Built - Main Features

2.1 User System

User Registration: New users can create accounts with username, email, password
Login/Logout: Users can log in and out of their accounts
User Sessions: Website remembers who is logged in
User Profile: Basic profile page showing user information
Protected Pages: Some pages only work when logged in

2.2 Book Management

Book Display: Shows all books in a nice grid layout
Book Information: Each book shows title, author, price, picture, stock
Book Search: Users can search for books by title or author name
Stock Status: Shows "In Stock", "Low Stock", or "Out of Stock"
Book Details: Click on any book to see more information
Book Images: Each book has a cover picture

2.3 Shopping Cart

Add to Cart: Users can add books to their shopping cart
View Cart: See all items in cart with quantities and prices
Change Quantity: Increase or decrease how many books to buy
Remove Items: Delete books from cart
Stock Check: Can't add more books than available in stock
Cart Total: Shows total price of all items

2.4 Order System

Checkout: Complete purchase with shipping information
Order Creation: Converts cart items into actual orders
Order History: Users can see all their past orders
Order Details: Shows what books were ordered and when
Stock Updates: Book stock goes down when someone buys it
Order Statistics: Shows total books bought and money spent

2.5 Admin Features

Admin Panel: Special area for managing books and orders
Add Books: Admin can add new books to sell
Edit Books: Change book information, prices, stock
View Orders: See all customer orders
Data Validation: Prevents wrong data like negative prices

3. Technical Implementation

3.1 Database Design

The website uses 4 main data tables:
Book Table: Stores book information (title, author, price, stock, image)
Cart Table: Stores what each user has in their cart
Order Table: Stores completed purchases
OrderItem Table: Stores individual books in each order

3.2 Website Pages Built (11 pages total)

Home Page (list.html): Shows all books, search box
Book Detail (detail.html): Individual book information
Login Page (login.html): User login form
Register Page (registration.html): New user signup
Cart Page (cart.html): Shopping cart with items
Checkout Page (checkout.html): Order form
Orders Page (orders.html): Order history
Success Page (success.html): Order confirmation
About Page (about.html): Company information
Profile Page (profile.html): User account info
Base Template (base.html): Header and navigation for all pages

3.3 Programming Functions (15 functions)

home(): Shows book list with search
register(): Creates new user accounts
login_view(): Handles user login
logout_view(): Logs users out
detail(): Shows individual book details
add_to_cart(): Adds books to cart
cart(): Displays shopping cart
remove_from_cart(): Removes items from cart
update_quantity(): Changes item quantities
checkout(): Processes orders
orders(): Shows order history
about(): Shows about page
profile(): Shows user profile

4. Website Structure and Organization

4.1 File Organization

Main Project Folder/
bookshop/: Main Django application
books/: Book store functionality
static/: CSS and JavaScript files
media/: Book cover images (12 book images)
templates/: HTML page templates
Configuration files

4.2 Database Changes

The project has 5 database updates (migrations):
0001_initial: Initial setup of all tables
0002_alter_book_price_alter_book_stock: Added price and stock validation
0003_alter_book_price: Fixed price validation rules
0004_auto_20250616_2030: Added cart and order tables
0005_alter_cart_unique_together: Prevented duplicate cart items

5. Key Technical Features

5.1 User Authentication

Users must create accounts to buy books
Passwords are encrypted for security
Login status is remembered across pages
Some features only work when logged in

5.2 Data Validation

Book prices must be positive numbers
Stock quantities cannot be negative
Users cannot add more items than available stock
All forms check for valid input

5.3 Search System

Users can search by book title or author
Search works with partial matches
Results update automatically
Case-insensitive searching

5.4 Shopping Cart Logic

Each user has their own cart
Cart remembers items between visits
Automatic stock checking
Cannot add same book twice (increases quantity instead)

5.5 Order Processing

Converts cart items to permanent orders
Captures customer shipping information
Updates book stock automatically
Clears cart after successful order
Saves order history for users

6. Technical Problems Solved

Template Issues: Fixed CSS conflicts between pages
Cart Duplicates: Prevented same book being added multiple times
Stock Management: Real-time stock checking and updates
JavaScript Bugs: Fixed button behavior for out-of-stock items
Form Validation: Added proper error checking
Database Relationships: Proper connections between users, books, and orders
Template Syntax Errors: Fixed Django template tag spacing and completion
URL Parameter Issues: Corrected inconsistent parameter names between URLs and views
Model Validation: Added MinValueValidator for price and stock fields
Navigation Issues: Fixed header CSS conflicts in success page

7. What Works Well

Complete Shopping Flow: Users can browse, search, add to cart, and buy books
Data Safety: All information is properly validated and stored
User-Friendly: Easy to navigate and use
Stock Control: Prevents overselling of books
Order Tracking: Complete history of all purchases
Admin Control: Easy management of books and orders
Responsive Design: Works on different screen sizes
Search Functionality: Fast and accurate book searching
Cart Management: Smooth adding, removing, and updating of items
Order Statistics: Shows total books purchased and money spent

8. Project Files Summary

Total Templates: 11 HTML files
Total Views: 15 Python functions
Total Models: 4 database tables
Total Migrations: 5 database updates
Total Book Images: 12 cover images
CSS Files: 2 (main styles and admin validation)
JavaScript Files: 2 (base functionality and admin validation)
Database: SQLite with Django ORM
Admin Interface: Customized Django admin panel
URL Patterns: 13 different page routes

This Django bookshop project successfully implements all the core features needed for an online book store, from user registration to order completion. The website is fully functional and ready for use.
