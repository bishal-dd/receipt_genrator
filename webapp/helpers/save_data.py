from ..models import Profile, Receipt, Version, Service


class save_receipts():
    def save_profile(request, user_id):
        profile = Profile.objects.filter(user=user_id).first()

        # PROFILE
        company_name = request.POST.get('company_name')
        image = request.FILES.get('logo_image', None)
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        email = request.POST.get('email')
        city = request.POST.get('city')
        signature_image = request.FILES.get('signature_image', None)
        manual_signature_image = request.POST.get('manual_signature_image')

        if profile:
            # Update the existing profile
            profile.company_name = company_name
            if image:
                profile.logo_image = image
            profile.phone_no = phone_no
            profile.address = address
            profile.email = email
            profile.city = city
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
                signature_image=signature_image,
                manual_signature_image=manual_signature_image,
                user=user_id
            )

        profile.save()

    def save_service(request, receipt):
        descriptions = request.POST.getlist('description')
        rates = request.POST.getlist('rate')
        quantities = request.POST.getlist('quantity')
        cost_amounts = request.POST.getlist('cost_amount')

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

    def save_receipt(request, user_id):
        # RECEIPT
        recipient_name = request.POST.get('recipient_name')
        recipient_phone = request.POST.get('recipient_phone')
        amount = request.POST.get('amount')
        Journal_no = request.POST.get('Journal_no')
        user = user_id

        receipt = Receipt(
            recipient_name=recipient_name,
            recipient_phone=recipient_phone,
            amount=amount,
            Journal_no=Journal_no,
            user=user
        )

        receipt.save()
        save_receipts.save_service(request, receipt)

    def save_version(request, user_id):
        version = Version.objects.filter(user=user_id).first()

        if not version:
            version = Version(user=user_id)
            version.save()