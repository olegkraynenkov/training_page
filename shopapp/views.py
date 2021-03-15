from django.shortcuts import render

from shopapp.models import Product

def product(request):
    products = Product.objects.all()

    content = {'products': products}

    return render(request, 'shopapp/product.html', content)
