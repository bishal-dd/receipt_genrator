from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)


class Profile(BaseModel):
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


class Receipt(BaseModel):
    receipt_name = models.CharField(max_length=100, null=False)
    recipient_name = models.CharField(max_length=100, null=False)
    recipient_phone = models.IntegerField(null=False)
    amount = models.FloatField(null=False)
    Journal_no = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    total_amount = models.FloatField(null=False, default=0)


class Service(BaseModel):
    description = models.CharField(max_length=5000, null=False)
    rate = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)


class Version(BaseModel):
    mode = models.CharField(max_length=10, choices=[(
        'trial', 'trial'), ('paid', 'paid')], default='trial')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    use_count = models.IntegerField(null=False, default=0)
