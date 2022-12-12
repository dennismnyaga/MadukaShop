from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ProductPhoto)
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(ProductCategory)

admin.site.register(ShopCategory)
admin.site.register(Shop)
admin.site.register(ShopPhoto)