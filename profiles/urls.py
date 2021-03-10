from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 14689964ad0ebf1acd045a1ba2615433f58689f5
