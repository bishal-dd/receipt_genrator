from ..models import Profile, Receipt, Version, Service
from ..validation.allow_empty import allow_empty
from .convert_image_url import convert_image


def save_profile(request, user_id):
    profile = Profile.objects.filter(user=user_id).first()

    # PROFILE
    company_name = request.POST.get('company_name')
    image = request.FILES.get('logo_image', None)
    phone_no = request.POST.get('phone_no')
    address = request.POST.get('address')
    email = request.POST.get('email')
    city = request.POST.get('city')
    title = request.POST.get('title')
    signature_image = request.FILES.get('signature_image', None)
    manual_signature_image = request.POST.get('manual_signature_image')

    if image:
        image = convert_image(image)

    if signature_image:
        signature_image = convert_image(signature_image)

    phone_no = allow_empty(phone_no)
    if profile:
        # Update the existing profile
        profile.company_name = company_name
        if image:
            profile.logo_image = image

        profile.phone_no = phone_no
        profile.address = address
        profile.email = email
        profile.city = city
        profile.title = title
        if signature_image:
            profile.signature_image = signature_image
        profile.manual_signature_image = manual_signature_image
    else:
        # Create a new profile
        profile = Profile(
            company_name=company_name,
            logo_image=image,
            phone_no=phone_no,
            address=address,
            email=email,
            city=city,
            title=title,
            signature_image=signature_image,
            manual_signature_image=manual_signature_image,
            user=user_id
        )

    profile.save()

    return profile


def save_service(request, receipt):
    descriptions = request.POST.getlist('description')
    rates = request.POST.getlist('rate')
    quantities = request.POST.getlist('quantity')
    cost_amounts = request.POST.getlist('cost_amount')

    services = []  # Create an empty list to store the saved services

    for description, rate, quantity, cost_amount in zip(descriptions, rates, quantities, cost_amounts):
        if description:  # Check if the field is not empty
            service = Service(
                description=description,
                rate=rate,
                quantity=quantity,
                amount=cost_amount,
                receipt=receipt  # You can associate these services with the same receipt
            )
            service.save()
            # Append the saved service to the list
            services.append(service)
    return services


def save_receipt(request, user_id):
    # RECEIPT
    recipient_name = request.POST.get('recipient_name')
    receipt_name = request.POST.get('receipt_name')
    recipient_phone = request.POST.get('recipient_phone')
    amount = request.POST.get('amount')
    journal_no = request.POST.get('Journal_no')
    date = request.POST.get('date')
    total_amount = request.POST.get('total_amount')
    user = user_id

    journal_no = allow_empty(journal_no)
    total_amount = allow_empty(total_amount)

    receipt = Receipt(
        recipient_name=recipient_name,
        recipient_phone=recipient_phone,
        amount=amount,
        Journal_no=journal_no,
        date=date,
        receipt_name=receipt_name,
        user=user,
        total_amount=total_amount
    )

    receipt.save()
    services = save_service(request, receipt)

    # Return a tuple containing the receipt and the associated services
    return receipt, services


def save_version(request, user_id):
    version = Version.objects.filter(user=user_id).first()

    if not version:
        version = Version(user=user_id)
        version.save()
        return version
    return version
