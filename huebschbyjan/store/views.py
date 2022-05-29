from multiprocessing import context
import re
from urllib import request
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import CreateUserForm, PaymentForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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
def item(request):
    context = {}
    return render(request,'store/item.html')


def contact(request):
    context = {}
    return render(request,'store/contact-us.html')

@login_required(login_url='login')
def contact_in(request):
    context = {}
    return render(request,'store/contact-us-in.html')

@login_required(login_url='login')
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {'items':items, 'order':order}
    return render(request,'store/cartpage.html', context)

@login_required(login_url='login')
def menu(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'store/menupage.html', context)

def logoutuser(request):
    logout(request)
    return redirect('home')

