from multiprocessing import context
from django.shortcuts import render

def home(request):
    context = {}
    return render(request,'store/home.html')

def login(request):
    context = {}
    return render(request,'store/login.html')

def register(request):
    context = {}
    return render(request,'store/register.html')

def payment(request):
    context = {}
    return render(request,'store/payment.html')

def item(request):
    context = {}
    return render(request,'store/item.html')

def contact(request):
    context = {}
    return render(request,'store/contact-us.html')

