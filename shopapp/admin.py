from django.contrib import admin

from shopapp.models import Product, ProductCategory


admin.site.register(ProductCategory)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Product, ProductAdmin)
