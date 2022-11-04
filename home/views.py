from django.shortcuts import render


def index(request): 
    """ A view to return the index page"""
    return render(request, 'home/index.html')


def about(request): 
    """ A view to return the about page"""
    return render(request, 'home/about.html')


def plans(request): 
    """ A view to return the about page"""
    return render(request, 'home/plans.html')


def prices(request): 
    """ A view to return the about page"""
    return render(request, 'home/prices.html')