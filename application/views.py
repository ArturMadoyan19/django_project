from django.shortcuts import render, redirect
from .models import Login
from registration.models import Reg

def info_view(request):
    return render(request, "application/index.html")

def login_view(request):
    login = ''
    password = ''
    success = False
    if request.method == 'POST':
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')
        if login == Reg.login and password == Reg.password:
            success = True
    return render(request, 'application/index.html',
                    {'login_value': login, 
                    'password_value': password,
                    'surname_value': Reg.surname,
                    'email_value': Reg.email,
                    'success':success})
        
        

