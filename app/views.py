from http.client import responses
from django.http import HttpResponse
from django.shortcuts import render



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
    return render(request, 'app/registration.html')