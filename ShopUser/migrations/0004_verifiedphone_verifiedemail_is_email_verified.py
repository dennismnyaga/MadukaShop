# Generated by Django 4.1.3 on 2024-03-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopUser', '0003_verifiedemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifiedPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('otp_number', models.CharField(max_length=200)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('timeout', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='verifiedemail',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]