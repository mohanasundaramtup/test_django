from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from .forms import LogInForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
def home(request):
    return render(request,"main_app/home.html",{})

def ticket(request):
    return render(request,"main_app/ticket.html",{})

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_1 = authenticate(request, username=username, password=password)
        print(username,password)
        if user_1 is not None:
            auth_login(request, user_1)
            sub="TESTING"
            msg="BODY"
            e_f=settings.EMAIL_HOST_USER
            r_m=["gokulnath.bj@gmail.com",]
            send_mail(sub,msg,e_f,r_m)
            return redirect('home')
        else:
            return HttpResponse(username,password)
   
    else:
        form=LogInForm()
        context={"form":form}

    return render(request,"main_app/login.html",context)

def logout(request):
    
    auth_logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        f = UserCreationForm()
    return render(request, 'main_app/signup.html', {'form': f})