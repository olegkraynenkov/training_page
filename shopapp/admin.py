from django.contrib import admin

from shopapp.models import Product, ProductCategory


admin.site.register(ProductCategory)
admin.site.register(Product)
