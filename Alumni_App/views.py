from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def Login(request):
    return render(request, 'Login.html')

def Logout(request):
    # logout(request)
    return render(request, 'Login.html')

def Register(request):
    return render(request, 'Register.html')
    
def Contact(request):
    return render(request, 'Contact.html')

def Profile(request):
    context = {
        'BreadCrumb' : 'Profile'
    }
    return render(request, 'Admin/Profile.html', context)

def Dashboard(request):
    context = {
        'BreadCrumb' : 'Dashboard'
    }
    return render(request, 'Admin/Dashboard.html', context)