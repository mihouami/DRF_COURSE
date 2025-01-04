from django.urls import path  # Importing the path function to define URL patterns.
from .views import product_info, ProductList, ProductDetail, OrderList, UserOrderList # Importing view functions for the API.

# Define URL patterns for the API endpoints.
urlpatterns = [
    path('products/', ProductList.as_view()),  # Endpoint to list all products.
    path('products/<int:product_id>/', ProductDetail.as_view()),  # Endpoint to retrieve details of a specific product by its ID (pk).
    path('product_info/', product_info),  # Endpoint to list all products.
    path('orders/', OrderList.as_view()),  # Endpoint to list all orders.
    path('user-orders/', UserOrderList.as_view(), name='user-orders'), # Endpoint to list all orders for the authenticated user.
]
