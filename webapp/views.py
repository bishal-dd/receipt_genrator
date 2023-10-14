from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Profile, Receipt, Version, Service


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("/")


def save_data(request):
    if request.method == 'POST':

        # PROFILE
        company_name = request.POST.get('')
        image = request.FILES['image']
        phone_no = request.POST.get('')
        address = request.POST.get('')
        email = request.POST.get('')
        city = request.POST.get('')
        signature_image = request.POST.get('')

        # RECEIPT
        recipient_name = request.POST.get('')
        recipient_phone = request.POST.get('')
        amount = request.POST.get('')
        Journal_no = request.POST.get('')
        # user =

        # SERVICE
        description = request.POST.get('')
        rate = request.POST.get('')
        quantity = request.POST.get('')
        # receipt =

        # VERSION
        # user =
