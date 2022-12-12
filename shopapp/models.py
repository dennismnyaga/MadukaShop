from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

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
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
   

    def __str__(self):
        return self.name



class ShopPhoto(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return self.shop

class ShopCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
   

    def __str__(self):
        return self.name



class ShopPhoto(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image')


    def __str__(self):
        return self.shop.name

class Product(models.Model):
    ad_title = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # condition = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


    def __str__(self):
        return self.ad_title



class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image')


    def __str__(self):
        return self.name


# ===========================================================================================================

