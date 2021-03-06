from email.policy import default
from typing import Text
from django.forms import ModelForm, TextInput, ChoiceField, Textarea
from .models import Customer, Shipping, ContactUs
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
        username = forms.CharField(max_length=200,
            widget=forms.TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id':"floatingInputName",
                'placeholder':"Full Name",
                'autofocus' : True
            })
        )

        email = forms.CharField(max_length=200,
            widget=forms.TextInput(attrs={
                'type': "email",
                'class': "form-control",
                'id':"floatingInputEmail",
                'placeholder':"name@example.com",
                
            }),
        )

        password1 = forms.CharField(max_length=200,
            widget=forms.TextInput(attrs={
                'type': "password",
                'class': "form-control",
                'id':"floatingPassword",
                'placeholder':"Password",
            }), 
        )

        password2 = forms.CharField(max_length=200,
            widget=forms.TextInput(attrs={
                'type': "password",
                'class': "form-control",
                'id':"floatingPasswordConfirm",
                'placeholder':"Confirm Password",
            }),   
        )

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']


class PaymentForm(ModelForm):
    address = forms.CharField(max_length=200,
            widget=forms.TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id':"address",
                'placeholder':"Address",
            })
        )

    contact = forms.CharField(max_length=200, required=True,
            widget=forms.TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id':"contact",
                'placeholder':"Number",
            })
        )   
    payment_method = forms.ChoiceField(choices=Shipping.payment_type,
            widget=forms.RadioSelect
    )   

    class Meta:
        model = Shipping
        fields = ['address', 'contact', 'payment_method']
    
class ContactUsForm(ModelForm):
    name = forms.CharField(max_length=200, required=True,
            widget=forms.TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id':"name",
                'placeholder':"Name",
            })
        )

    email = forms.CharField(max_length=200, required=True,
            widget=forms.TextInput(attrs={
                'type': "email",
                'class': "form-control",
                'id':"emailAddress",
                'placeholder':"Email Address",
            })
        )   

    message = forms.CharField(max_length=10000, required=True,
            widget=forms.Textarea(attrs={
                'type': "text",
                'class': "form-control",
                'id':"message",
                'placeholder':"Message",
                'style':"height: 10rem;"
            })
        )  

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

