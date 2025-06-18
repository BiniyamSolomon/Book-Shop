from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [
 path('', views.home, name='home'),
 path('register', views.register, name='register'),
 path('login/', views.login_view, name='login_view'),
 path('logout/', views.logout_view, name='logout_view'),
 path('about/', views.about, name='about'),
 path('detail/<int:id>', views.detail, name='detail'),
 path('add/<int:book_id>', views.add_to_cart, name='add_to_cart'),#this is to add in the cart
 path('cart/', views.cart, name='cart'),
 path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
 path('update_quantity/<int:cart_item_id>/', views.update_quantity, name='update_quantity'),
 path('checkout/', views.checkout, name='checkout'),
 path('orders/', views.orders, name='orders'),


 

]