from django.http import HttpResponse
from django.urls import path
from .views import HomePage , UserPage

urlpatterns = [
    path('home', HomePage),
    path('user', UserPage),
    
]
