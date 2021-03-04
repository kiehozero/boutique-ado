from django.urls import path, include
from . import views


# . means to import from the current directory

urlpatterns = [
    path('', views.all_products, name='products')
]
