from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

class LogInForm(ModelForm):
    class Meta:
        model=User
        fields =["username","password"]

class UserCreateCustomform(UserCreationForm):
    email=forms.EmailField(max_length = 254)
    class Meta:
        model=User
        fields=["username","email"]