from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class CustomuserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'from-control','placeholder':'username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))

    class Meta:
        model=User
        fields =['username','email','password1','password2']


     
        