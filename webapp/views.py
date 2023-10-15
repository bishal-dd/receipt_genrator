from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Profile, Receipt, Version, Service
from django.contrib.auth.decorators import login_required
from .helpers.save_data import save_receipts


def index(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = Profile.objects.filter(user=request.user).first()

    return render(request, 'index.html', {'user_profile': user_profile})


def login(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def save_data(request):
    if request.method == 'POST':
        user_id = request.user
        save_receipts.save_profile(request, user_id)
        save_receipts.save_receipt(request, user_id)
        save_receipts.save_version(request, user_id)

        return redirect('webapp:index')
