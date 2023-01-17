from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Location)
admin.site.register(Shop)
admin.site.register(ShopCategory)
admin.site.register(Like)
admin.site.register(ShopPhoto)