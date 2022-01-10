from django.contrib import admin
from django.urls import path
from .views import homeView

urlpatterns = [
    path('home/', homeView, name='home'),
]