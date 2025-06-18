from django.contrib import admin
from django import forms
from .models import Book, Cart, Order, OrderItem

# Register your models here.

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'price': forms.NumberInput(attrs={
                'min': '0',
                'step': '0'
            }),
            'stock': forms.NumberInput(attrs={
                'min': '0',
                'step': '1'
            })
        }
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError()
        return price
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError()
        return stock



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ['title', 'author', 'price', 'stock']
    search_fields = ['title', 'author']
    list_filter = ['stock']
   

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'quantity', 'created_at']
    list_filter = ['user', 'created_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at', 'total_amount']
    list_filter = ['status', 'created_at', 'user']
    search_fields = ['user__username']
    list_editable = ['status']
    readonly_fields = ['created_at', 'total_amount']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'quantity', 'price']
    list_filter = ['order', 'book']
    search_fields = ['order__id', 'book__title']



