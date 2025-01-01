# from django.http import JsonResponse  # Unused import; can be used for returning JSON responses if needed.
from django.shortcuts import get_object_or_404  # Utility function to get an object or return a 404 error.
from .serializers import ProductSerializer, OrderSerializer  # Importing serializers for Product and Order models.
from .models import Product, Order  # Importing Product and Order models.
from rest_framework.response import Response  # DRF's Response class to standardize API responses.
from rest_framework.decorators import api_view  # Decorator to define API views supporting specific HTTP methods.

##### PRODUCTS VIEWS #####
@api_view(['GET'])  # Specifies that this view only handles GET requests.
def product_list(request):
    # Retrieve all products from the database.
    products = Product.objects.all()
    # Serialize the list of products.
    serializer = ProductSerializer(products, many=True)
    # Return the serialized data as a response.
    # return JsonResponse({'data': serializer.data})  # Alternative way to return JSON data.
    return Response(serializer.data)


@api_view(['GET'])  # Specifies that this view only handles GET requests.
def product_detail(request, pk):
    # Retrieve a product by its primary key or return a 404 error if not found.
    # product = Product.objects.get(id=pk)  # Direct retrieval without 404 handling.
    product = get_object_or_404(Product, id=pk)
    # Serialize the product instance.
    serializer = ProductSerializer(product)
    # Return the serialized data as a response.
    return Response(serializer.data)


##### ORDERS VIEWS #####
@api_view(['GET'])  # Specifies that this view only handles GET requests.
def order_list(request):
    # Retrieve all orders from the database.
    orders = Order.objects.all()
    # Serialize the list of orders.
    serializer = OrderSerializer(orders, many=True)
    # Return the serialized data as a response.
    return Response(serializer.data)
