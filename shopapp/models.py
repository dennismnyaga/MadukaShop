from django.db import models
import uuid

from django.contrib.auth import get_user_model

User = get_user_model()



class ProductCategory(models.Model):
   
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category_images', blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
   
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name




class ShopCategory(models.Model):
   
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Shop(models.Model):
   
    owner = models.ForeignKey( User,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    registered_on = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.name



class ShopPhoto(models.Model):
   
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shopimages')
    image = models.ImageField(upload_to='product_images')


    def __str__(self):
        return self.shop.name

class Product(models.Model):
   
    owner = models.ForeignKey( User,  on_delete=models.CASCADE,  related_name='products')
    ad_title = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
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




class NewsLetterEmails(models.Model):
   
    email = models.CharField(max_length=200)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
# ===========================================================================================================