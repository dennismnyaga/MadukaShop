# Generated by Django 4.1.3 on 2022-12-18 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_shop_shopcategory_shopphoto_shop_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='condition',
        ),
    ]