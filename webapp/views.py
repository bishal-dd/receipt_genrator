from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Profile, Receipt, Version, Service
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .helpers import save_data
from .pagination.pagination import pagination
from .helpers.pdf_generation import pdf_generation
from .filters.year_month_filter import year_month_filter
from .helpers.check_version import CheckVersion, add_count
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = Profile.objects.filter(user=request.user).first()

    return render(request, 'index.html', {'user_profile': user_profile})


def login(request):
    return render(request, 'login.html')


def trial_period(request):
    return render(request, 'trial_period.html')


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def receipts_view(request):
    user_receipts = None
    if request.user.is_authenticated:
        user_id = request.user.id
        # Get the selected year from the request
        year = request.GET.get('year')
        # Get the selected month from the request
        month = request.GET.get('month')
        user_receipts = Receipt.objects.filter(
            user_id=user_id).order_by('-id')
        user_receipts = year_month_filter(user_receipts, year, month)
        total_amount = user_receipts.aggregate(
            Sum('amount'))['amount__sum'] or 0
    user_receipts = pagination(request, user_receipts, 10)

    return render(request, 'view_receipts.html', {'user_receipts': user_receipts, 'total_amount': total_amount})


@login_required
def generate_pdf(request):
    if request.method == 'POST':
        user_id = request.user
        version = save_data.save_version(request, user_id)
        mode = CheckVersion(user_id).mode()
        use_count = CheckVersion(user_id).use_count()

        if mode == "paid" or (mode == "trial" and use_count <= 5):
            add_count(version)
            profile = save_data.save_profile(request, user_id)
            receipt, services = save_data.save_receipt(request, user_id)

            data = {
                "profile": profile,
                "receipt": receipt,
                "services": services,
            }
            pdf_generation(data)
            return pdf_generation(data)
        else:
            return redirect("webapp:trial_period")


def save_receipt(request):
    if request.method == 'POST':
        user_id = request.user
        version = save_data.save_version(request, user_id)
        mode = CheckVersion(user_id).mode()
        use_count = CheckVersion(user_id).use_count()

        if mode == "paid" or (mode == "trial" and use_count <= 5):

            add_count(version)
            save_data.save_profile(request, user_id)
            save_data.save_receipt(request, user_id)

            return JsonResponse({"message": "Data saved successfully"})  # Return a JSON response
        else:
            return JsonResponse({"message": "Trial attempts up"})


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


def toggle_user_status(request, pk):
    user = get_object_or_404(User, pk=pk)

    # Toggle the user status attribute (e.g., is_staff, is_superuser)
    user.is_staff = not user.is_staff
    user.save()

    return redirect("admin:webapp_user_changelist")


def change_mode(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        version = Version.objects.get(user=user)
        if version.mode == "trial":
            version.mode = "paid"
        else:
            version.mode = "trial"
        version.save()
    except User.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('admin:auth_user_changelist'))


def delete_sign(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        if profile.signature_image:
            # Delete the image file from the server
            profile.signature_image.delete()
            return JsonResponse({"message": "Signature deleted successfully"})
        else:
            return JsonResponse({"message": "Signature not found"})
    except Profile.DoesNotExist:
        return JsonResponse({"message": "User profile not found"}, status=404)
