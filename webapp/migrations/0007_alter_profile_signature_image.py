# Generated by Django 3.2.12 on 2023-10-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_version_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='signature_image',
            field=models.CharField(max_length=20000, null=True),
        ),
    ]
