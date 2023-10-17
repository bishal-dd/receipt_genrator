from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Profile, Receipt, Version, Service
from django.contrib.auth.decorators import login_required
from .helpers import save_data
from .pagination.pagination import pagination
from .helpers.pdf_generation import pdf_generation
from .filters.year_month_filter import year_month_filter
from django.contrib import messages


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
def receipts_view(request):
    user_receipts = None
    if request.user.is_authenticated:
        user_id = request.user.id
        year = request.GET.get('year')  # Get the selected year from the request
        month = request.GET.get('month')  # Get the selected month from the request
        user_receipts = Receipt.objects.filter(user_id=user_id).order_by('date')
        user_receipts = year_month_filter(user_receipts, year, month)
        total_amount = user_receipts.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    user_receipts = pagination(request, user_receipts, 10)

    return render(request, 'view_receipts.html', {'user_receipts': user_receipts, 'total_amount': total_amount})


@login_required
def generate_pdf(request):
    if request.method == 'POST':
        user_id = request.user
        version = save_data.save_version(request, user_id)
        profile = save_data.save_profile(request, user_id)
        receipt, services = save_data.save_receipt(request, user_id)

        data = {
            "profile": profile,
            "receipt": receipt,
            "services": services,
        }
        pdf_generation(data)
        return pdf_generation(data)


def save_receipt(request):
    if request.method == 'POST':
        user_id = request.user
        save_data.save_version(request, user_id)
        save_data.save_version(request, user_id)
        save_data.save_profile(request, user_id)
        save_data.save_receipt(request, user_id)

    return redirect('webapp:index')


def generate_individual_receipt(request, id):
    receipt = Receipt.objects.filter(id=id).first()
    profile = Profile.objects.filter(user=request.user).first()
    services = Service.objects.filter(receipt_id=id)
    data = {
        "profile": profile,
        "receipt": receipt,
        "services": services,
    }

    pdf_generation(data)

    # Return the result of the pdf_generation function
    return pdf_generation(data)