from django import forms
from django.shortcuts import render, redirect
from django.forms.widgets import TextInput
from employee.models import Employee, Position
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse  
from warsztat import settings
from django.core.mail import send_mail  
from django.template.loader import render_to_string  
from django.core.mail import EmailMessage  

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


