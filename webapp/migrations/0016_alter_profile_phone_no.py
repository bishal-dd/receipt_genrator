# Generated by Django 3.2.12 on 2023-10-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_delete_customemailaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]
