# Generated by Django 4.1.3 on 2024-03-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopUser', '0002_customuser_forgot_password_token_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifiedEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('otp_number', models.CharField(max_length=200)),
                ('timeout', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]