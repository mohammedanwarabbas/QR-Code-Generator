from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name="index"),
    path('generateqr/', views.generateqr, name="generateqr"),
]