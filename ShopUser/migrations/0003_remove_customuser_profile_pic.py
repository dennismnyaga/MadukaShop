# Generated by Django 4.1.3 on 2022-12-21 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopUser', '0002_customuser_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_pic',
        ),
    ]