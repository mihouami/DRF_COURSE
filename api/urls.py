from django.urls import path  # Importing the path function to define URL patterns.
from .views import product_list, product_detail, order_list  # Importing view functions for the API.

# Define URL patterns for the API endpoints.
urlpatterns = [
    path('products/', product_list),  # Endpoint to list all products.
    path('products/<int:pk>/', product_detail),  # Endpoint to retrieve details of a specific product by its ID (pk).
    path('orders/', order_list),  # Endpoint to list all orders.
]
