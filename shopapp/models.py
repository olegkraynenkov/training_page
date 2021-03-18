from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_image', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    categoty = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
