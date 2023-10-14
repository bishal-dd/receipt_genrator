from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    company_name = models.CharField(max_length=100, null=False)
    logo_image = models.ImageField(upload_to='images/')
    phone_no = models.IntegerField(null=False)
    address = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    signature_image = models.ImageField(upload_to='images/')
    slug = models.SlugField(null=False)


class Receipt(models.Model):
    recipient_name = models.CharField(max_length=100, null=False)
    recipient_phone = models.IntegerField(null=False)
    amount = models.FloatField(null=False)
    Journal_no = models.IntegerField(null=True)
    user = models.ForeignKey(Foreign_User, on_delete=models.CASCADE)


class Service(models.Model):
    description = models.CharField(max_length=5000, null=False)
    rate = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    Amount = models.IntegerField(null=False)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)


