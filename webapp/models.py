from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    company_name = models.CharField(max_length=100, null=False)
    logo_image = models.ImageField(upload_to='images/')
    phone_no = models.IntegerField(null=False)
    address = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    signature_image = models.ImageField(
        upload_to='images/', null=True, blank=True)
    manual_signature_image = models.CharField(max_length=20000, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=False)


class Receipt(models.Model):
    recipient_name = models.CharField(max_length=100, null=False)
    recipient_phone = models.IntegerField(null=False)
    amount = models.FloatField(null=False)
    Journal_no = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Service(models.Model):
    description = models.CharField(max_length=5000, null=False)
    rate = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)


class Version(models.Model):
    mode = models.CharField(max_length=10, choices=[(
        'trial', 'trial'), ('paid', 'paid')], default='trial')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    use_count = models.IntegerField(null=False, default=0)
