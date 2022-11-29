from django.shortcuts import render
from django import forms
from .forms import NewsletterForm
from django.shortcuts import redirect


def index(request): 
    """ A view to return the index page"""
    return render(request, 'home/index.html')


def about(request): 
    """ A view to return the about page"""
    return render(request, 'home/about.html')
