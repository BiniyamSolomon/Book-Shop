from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.00)]  
    )
    description = models.TextField()
    image = models.ImageField()
    stock = models.IntegerField(
        default=1,
        validators=[MinValueValidator(0)]  
    )
    
    # def clean(self):
    #     if self.price <= 0:
    #         raise ValidationError("Price must be greater than 0")
    #     if self.stock < 0:
    #         raise ValidationError("Stock cannot be negative")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'book')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='processing')
    shipping_address = models.TextField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)