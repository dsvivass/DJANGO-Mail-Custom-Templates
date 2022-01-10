from django.contrib import admin
from django.urls import path
from .views import sendEmailAPIView

urlpatterns = [
    path('sendEmail/', sendEmailAPIView.as_view()),
]