from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Profile,Receipt,Version,Service


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("/")

def save_data(request):
    if request.method == 'POST':
