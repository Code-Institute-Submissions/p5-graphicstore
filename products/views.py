from django.shortcuts import render


def all_products(request): 
    """ A view for all products, including sorting and search queries """
    return render(request, 'products/products.html', contact)