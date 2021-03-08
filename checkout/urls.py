from django.urls import path
from . import views
from .webhooks import webhook


# . means to import from the current directory

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>',
        views.checkout_success,
        name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'),
]
