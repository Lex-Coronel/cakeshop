import imp
from django.db import models
from django.contrib.auth.models import User
from numpy import true_divide
from django.forms import ModelForm

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_subtotal(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems]) + 60
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    dedication = models.CharField(max_length=500)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class Shipping(models.Model):
    COD = 'COD'
    GCASH = 'GCASH'
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    contact = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    payment_type = [
        (COD, 'COD'), 
        (GCASH, 'GCASH')
    ]
    payment_method = models.CharField(max_length=200, choices=payment_type, default=COD)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

