from django.shortcuts import render
from django import forms
from .forms import NewsletterForm
from django.shortcuts import redirect


def index(request): 
    """ A view to return the index page"""
    form = NewsletterForm()
    context = { 
        'form': form,
    }

    return render(request, 'home/index.html', context)


def about(request): 
    """ A view to return the about page"""
    return render(request, 'home/about.html')


def subscribe(request):
    """ """
    form = NewsletterForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')