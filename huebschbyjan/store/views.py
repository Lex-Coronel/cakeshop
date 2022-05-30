from multiprocessing import context
import re
from urllib import request
from django.http import JsonResponse
from django.shortcuts import redirect, render
from numpy import product
from .models import *
from django.contrib import messages
from .forms import ContactUsForm, CreateUserForm, PaymentForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import json
import datetime
from .filters import *

def home(request):
    context = {}
    return render(request,'store/home.html')

@login_required(login_url='login')
def index(request):
    context = {}
    return render(request,'store/index.html')

def userlogin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    context = {}
    return render(request,'store/userlogin.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            return redirect('index')

    context = {'form': form}
    return render(request,'store/register.html', context)

@login_required(login_url='login')
def payment(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    form = PaymentForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {'items':items, 'order':order, 'form':form}
    return render(request,'store/payment.html', context)

@login_required(login_url='login')
def item(request,pk):
    product_id = Product.objects.get(id=pk)

    context = {'product_id':product_id}
    return render(request,'store/item.html', context)


def contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'store/contact-us.html', context)

@login_required(login_url='login')
def contact_in(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    return render(request,'store/contact-us-in.html',context)

@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        products = Product.objects.all()
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'products': products, 'items':items, 'order':order, 'cartItems':cartItems, 'items':items}
    return render(request,'store/cartpage.html', context)

@login_required(login_url='login')
def menu(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        products = Product.objects.all()
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    cakeFilter = ProductFilter(request.GET, queryset=products)
    products = cakeFilter.qs
    
    context = {'products':products, 'cakeFilter': cakeFilter, 'cartItems':cartItems, 'items':items}
    return render(request,'store/menupage.html', context)

def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def deleteItem(request, pk):
    order = OrderItem.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('cartpage')

    context = {'order': order}
    return render(request, 'store/deleteItem.html', context)

def addtocart(request):
    data = json.loads(request.body)
    productId = data['productId']
    dedication = data['dedicationForm']['dedication']
    quantity = data['dedicationForm']['quantity']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'create':
        orderItem.product = product
        orderItem.order = order
        orderItem.quantity = int(quantity)
        orderItem.dedication = dedication
    else:
        orderItem.quantity = (orderItem.quantity + int(quantity))
        orderItem.dedication = dedication
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)

def delivering(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['total'])
    order.transaction_id = transaction_id

    order.complete = True
    order.save()

    Shipping.objects.create(
        customer=customer,
        order=order,
        contact=data['paymentForm']['number'],
        address=data['paymentForm']['address'],
        #payment_type=data['paymentForm']['method']
    )

    return JsonResponse('Order has been payed', safe=False)