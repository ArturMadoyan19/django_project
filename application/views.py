from django.shortcuts import render, redirect
from .models import Login

def info_view(request):
    return render(request, "application/index.html")

def login_view(request):
    login = ''
    password = ''
    success = False
    if request.method == 'POST':
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')
        if login == "Artur" and password == "Madoyan":
            success = True
    return render(request, 'application/index.html',
                    {'login_value': login, 
                    'password_value': password,
                    'success':success})
        

