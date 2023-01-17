from django.db import models
import uuid

from django.contrib.auth import get_user_model

User = get_user_model()

#from ShopUser.models import CustomUser

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# class ShopCategory(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


# class Shop(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     description = models.CharField(max_length=200)
   

#     def __str__(self):
#         return self.name



# class ShopPhoto(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_image')

#     def __str__(self):
#         return self.shop

class ShopCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Shop(models.Model):
    owner = models.ForeignKey( User,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    registered_on = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.name



class ShopPhoto(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_images')
    image = models.ImageField(upload_to='product_image')


    def __str__(self):
        return self.shop.name

class Product(models.Model):
    owner = models.ForeignKey( User,  on_delete=models.CASCADE,  related_name='products')
    ad_title = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_products', through='Like')
    views = models.PositiveIntegerField(default=0)



    def update_views(self):
        self.views += 1
        self.save(update_fields=['views'])


    def __str__(self):
        return self.ad_title


class ProductImage(models.Model):
    product = models.ForeignKey('Product',  on_delete=models.CASCADE, related_name='images' )
    image = models.ImageField(upload_to='product_images')
    
    def __str__(self):
        return self.product.ad_title


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.ad_title

# class ProductPhoto(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_image')


#     def __str__(self):
#         return self.name


# ===========================================================================================================

