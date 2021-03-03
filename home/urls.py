from django.contrib import admin
from django.urls import path, include
from . import views


# . means to import from the current directory

urlpatterns = [
    path('', views.index, name="home")
]
