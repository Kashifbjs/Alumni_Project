from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms

# Create your views here.
def Login(request):
    form = forms.Login_Form
    if request.method == 'POST':
        form = forms.Login_Form(request.POST)
        if form.is_valid():

            User_Name = form.cleaned_data['User_Name']
            Password = form.cleaned_data['Password']

            User = authenticate(request, username = User_Name, password = Password)
            if User is not None and User.is_active:
                login(request, user=User)
                return redirect('Dashboard')
            else:
                context = {
                    'Msg' : 'Incorrect User Name or Password!',
                    'form' : form,
                    'Form_Type' : 'Login'
                }
            return render(request, 'FormPage.html', context)
    else:
        context = {
            'form' : form,
            'Form_Type' : 'Login'
        }
        return render(request, 'FormPage.html', context)

@login_required(login_url='Login')
def Logout(request):
    logout(request)
    return redirect('Login')

def Register(request):
    form = forms.Register_Form
    if request.method == 'POST':
        form = forms.Register_Form(request.POST)
        if form.is_valid():
            User_Name = form.cleaned_data['User_Name']
            First_Name = form.cleaned_data['First_Name']
            Last_Name = form.cleaned_data['Last_Name']
            Email = form.cleaned_data['Email']
            Password = form.cleaned_data['Password']
            Password2 = form.cleaned_data['Password2']
            if Password == Password2:
                print('User already exists')
            Chk_Role = form.cleaned_data['Chk_Role']
            if Chk_Role == 'alumni':
                Chk_Role = 1
            elif Chk_Role == 'student':
                Chk_Role = 2
            elif Chk_Role == 'faculty':
                Chk_Role = 3
            if User.objects.filter(username = User_Name).exists():
                context = {
                    'Msg' : 'Username already Exist!',
                    'form' : form,
                    'Form_Type' : 'Register'
                }
                print('User already exists')
                return render(request, 'FormPage.html' , context)
            elif User.objects.filter(email = Email).exists():
                context = {
                    'Msg' : 'Email already Exist!',
                    'form' : form,
                    'Form_Type' : 'Register'
                }
                print('Email already Exist!')
                return render(request, 'FormPage.html' , context)
            else:
                New_User = User.objects.create_user(username = User_Name, email = Email, password = Password, first_name = First_Name, last_name = Last_Name)
            return redirect('Dashboard')
    else:
        context = {
            'form' : form,
            'Form_Type' : 'Register'
        }
        return render(request, 'FormPage.html', context)
    
def Contact(request):
    return render(request, 'Contact.html')

@login_required(login_url='Login')
def Profile(request):
    context = {
        'BreadCrumb' : 'Profile'
    }
    return render(request, 'Admin/Profile.html', context)

@login_required(login_url='Login')
def Dashboard(request):
    context = {
        'BreadCrumb' : 'Dashboard'
    }
    return render(request, 'Admin/Dashboard.html', context)