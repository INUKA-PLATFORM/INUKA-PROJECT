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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active = False 
            user.save()
            # form.save()
            messages.success(request, 'Registration successful. Please wait for admin approval to login.')
            return redirect('login')
        else:
            messages.error(request, 'Form is not valid. Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'auth/register.html', {'form': form})

def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Error validating form')
    return render(request, 'auth/login.html', {'form': form})

#admin
def admin(request):
    return render(request,'admin.html')

def user_logout(request):
    logout(request)
    return render(request, 'public/index.html')

