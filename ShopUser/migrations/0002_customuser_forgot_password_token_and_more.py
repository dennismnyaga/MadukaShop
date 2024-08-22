# Generated by Django 4.1.3 on 2024-03-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='forgot_password_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_phone_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
