# Generated by Django 4.1.3 on 2023-02-06 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0014_alter_shopphoto_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopphoto',
            name='image',
            field=models.ImageField(upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='shopphoto',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopimages', to='shopapp.shop'),
        ),
    ]
