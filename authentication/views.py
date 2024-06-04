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

#admin
def admin(request):
    return render(request,'admin.html')

def user_logout(request):
    logout(request)
    return render(request, 'public/index.html')

