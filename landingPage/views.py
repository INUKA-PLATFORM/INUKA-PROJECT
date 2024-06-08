from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {'nam':'David'})

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def concept_view(request):
    return render(request, 'concept.html')

def cause_view(request):
    return render(request, 'cause.html')

def ourcrew_view(request):
    return render(request, 'ourcrew.html')

def donate_view(request):
    return render(request, 'donate.html')

def aboutus_view(request):
    return render(request, 'aboutus.html')

def login_view(request):
    return render(request, 'login.html')

def admin_view(request):
    return render(request, 'admin.html')

def contact_view(request):
    return render(request, 'contact.html')

