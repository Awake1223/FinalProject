from http.client import responses
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def rating(request):
    return render(request, 'app/rating.html')

def currency(request):
    return render(request, 'app/currency.html')

def registration(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        mail = request.POST.get('mailAdress')
        password = request.POST.get('password')
        passwordRepeat = request.POST.get('passwordRepeat')
        if password != passwordRepeat:
            return HttpResponse("Пароли не совпадают!")
        else:
            app_profile = User(login = login, mail = mail, password = password)
            app_profile.save()
            return redirect('login')
    return render(request, 'app/registration.html')