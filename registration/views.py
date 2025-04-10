from django.shortcuts import render, redirect
from .models import Reg

# def index(request):
#     return render(request, "front/register.html")


def user_info(request):
    if request.method == "POST":
        Reg.login = request.POST.get('name', '')
        Reg.surname = request.POST.get('surname', '')
        Reg.email = request.POST.get('email', '')
        Reg.password = request.POST.get('password', '')

    return render(request, "front/register.html", {
        'name_value': Reg.login,
        'surname_value': Reg.surname,
        'email_value': Reg.email,
        'password_value': Reg.password
    })