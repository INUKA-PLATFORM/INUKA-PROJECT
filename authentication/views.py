from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'public/home.html')

def public_register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'auth/register.html', {'form': form, 'msg': msg})

def user_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_owner:
                login(request, user)
                return redirect('owner')
            elif user is not None and user.is_public:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            else:
                msg= 'invalid credentials'
        else:
            messages.info = 'error validating form'
    return render(request, 'auth/login.html', {'form': form, 'msg': msg})

#admin
def admin(request):
    return render(request,'admin.html')

def user_logout(request):
    logout(request)
    return render(request, 'public/index.html')

