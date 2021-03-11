from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # specifying that the below is an integer prevents an error where Django
    # uses the first URL it can find. In this case the product_detail path
    # would try to locate the word 'add'
    # from the add_product path as a product ID.
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
