from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to return products, search queries and sorting """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
