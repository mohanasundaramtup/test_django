from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from .forms import LogInForm
# Create your views here.
def home(request):
    return render(request,"main_app/home.html",{})

def ticket(request):
    return render(request,"main_app/ticket.html",{})

def login(request):
    uc=LogInForm()
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_1 = authenticate(request, username=username, password=password)
        print(username,password)
        if user_1 is not None:
            auth_login(request, user_1)
            return redirect('home')
        else:
            return HttpResponse(username,password)
    context={"uc":uc}
    return render(request,"main_app/login.html",context)

def logout(request):
    
    auth_logout(request)
    return redirect('home')
    
def signup(request):
    
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        "form":form
    }
    print(form)
    return render(request,"main_app/signup.html",context) 
 