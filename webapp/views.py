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
        company_name = request.POST.get('company_name')
        image = request.FILES['logo_image']
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        email = request.POST.get('email')
        city = request.POST.get('city')
        signature_image = request.FILES['signature_image']
        manual_signature_image = request.POST.get('manual_signature_image')

        profile = Profile(company_name=company_name, logo_image=image,
                          phone_no=phone_no, address=address, email=email, city=city, signature_image=signature_image, manual_signature_image=manual_signature_image)

        profile.save()

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

        return render(request, 'index.html')
