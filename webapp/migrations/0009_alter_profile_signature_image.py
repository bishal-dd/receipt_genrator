# Generated by Django 3.2.12 on 2023-10-14 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20231014_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='signature_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]