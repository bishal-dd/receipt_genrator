# Generated by Django 3.2.12 on 2023-10-14 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_version_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='mode',
            field=models.CharField(choices=[('trial', 'trial'), ('paid', 'paid')], default='trial', max_length=10),
        ),
    ]
