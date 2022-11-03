from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.index, name='about'),
    path('plans/', views.index, name='plans'),
    path('prices/', views.index, name='prices')
]
