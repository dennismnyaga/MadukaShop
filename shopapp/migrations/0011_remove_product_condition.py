# Generated by Django 4.1.3 on 2022-12-10 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0010_product_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='condition',
        ),
    ]
