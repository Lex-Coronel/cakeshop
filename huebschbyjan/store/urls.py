from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.register, name="register"),
    path('payment/', views.payment, name="payment"),
    path('item/<str:pk>/', views.item, name="item"),
    path('contact_us/', views.contact, name="contact-us"),
    path('contactus/', views.contact_in, name="contact-us-in"),
    path('cart/', views.cart, name="cartpage"),
    path('menu/', views.menu, name="menupage"),
    path('deleteItem/<str:pk>', views.deleteItem, name="deleteItem"),
    path('addtocart/', views.addtocart, name="addtocart"),
    path('delivering/', views.delivering, name="delivering"),
]
