from django.db import models




class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name






class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image')


    def __str__(self):
        return self.name