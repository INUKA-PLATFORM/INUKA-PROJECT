from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {'nam':'David'})

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')