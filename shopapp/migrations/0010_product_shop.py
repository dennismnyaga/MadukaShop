# Generated by Django 4.1.3 on 2022-12-10 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0009_alter_shop_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shopapp.shop'),
            preserve_default=False,
        ),
    ]
