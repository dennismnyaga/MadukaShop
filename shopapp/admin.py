from django.contrib import admin
from .models import *
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Location)
admin.site.register(Shop)
admin.site.register(ShopCategory)
admin.site.register(Like)
admin.site.register(ShopPhoto)
admin.site.register(NewsLetterEmails)


