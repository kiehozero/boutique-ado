from django.urls import path
from . import views


# . means to import from the current directory

urlpatterns = [
    path('', views.view_bag, name='view_bag')
]
