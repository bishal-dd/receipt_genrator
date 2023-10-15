from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from .models import Profile, Receipt, Version, Service
from django.contrib.auth.decorators import login_required
from .helpers.save_data import save_receipts
from .helpers.generate_receipt import generate_pdf


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
        pdf_generation()

        return pdf_generation()  # Return the result of the pdf_generation function


def pdf_generation():
    data = {
        "name": "Mama",
        "id": 18,
        "amount": 333,
    }
    pdf = generate_pdf('receipt_template.html', data)

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Report_for_%s.pdf" % (data['id'])
        content = f"inline; filename={filename}"
        response['Content-Disposition'] = content

        return response

    return HttpResponse("Page Not Found")
