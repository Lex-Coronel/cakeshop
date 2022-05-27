from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('payment/', views.payment, name="payment"),
    path('item/', views.item, name="item"),
    path('contactus/', views.contact, name="contact-us"),
]
