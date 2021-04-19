from django.shortcuts import render

from shopapp.models import Product, ProductCategory

def product(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    content = {'products': products, 'categories': categories}
    return render(request, 'shopapp/product.html', content)


def by_category(request, category_id):
    products = Product.objects.filter(category = category_id)
    category = ProductCategory.objects.all()
    current_category = ProductCategory.objects.get(pk=category_id)
    content = {
        'products': products, 'category': category, 'current_category': current_category
    }
    return render(request, 'shopapp/by_category.html', content)
