# Generated by Django 4.1.3 on 2022-12-24 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0009_product_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='likes',
        ),
    ]
