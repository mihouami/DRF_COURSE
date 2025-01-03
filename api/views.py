# from django.http import JsonResponse  # Unused import; can be used for returning JSON responses if needed.
from django.shortcuts import get_object_or_404  # Utility function to get an object or return a 404 error.
from .serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer  # Importing serializers.
from .models import Product, Order  # Importing Product and Order models.
from rest_framework.response import Response  # DRF's Response class to standardize API responses.
from rest_framework.decorators import api_view  # Decorator to define API views supporting specific HTTP methods.
from django.db.models import Max  # Importing Max aggregation function for database queries.
from rest_framework import generics # Importing generics for class-based views.


##### PRODUCTS VIEWS #####
class ProductList(generics.ListAPIView):
    queryset = Product.objects.exclude(stock__gt=0)  # Queryset to retrieve all products from the database.
    serializer_class = ProductSerializer


##### PRODUCT DETAIL VIEW #####
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()  # Queryset to retrieve all products from the database.
    serializer_class = ProductSerializer # Serializer class to use for serializing the retrieved product.
    lookup_url_kwarg = 'product_id'  # Custom URL keyword argument to retrieve the product ID from the URL.

##### ORDERS VIEWS #####
class OrderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')  # Queryset to retrieve all orders with related items and products.
    serializer_class = OrderSerializer # Serializer class to use for serializing the retrieved orders.



##### PRODUCT INFO VIEWS #####
@api_view(['GET'])  
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price'],
        'total_stock_value': sum(p.price * p.stock for p in products),
    })
    return Response(serializer.data)


'''
@api_view(['GET'])  # Specifies that this view only handles GET requests.
def product_list(request):
    products = Product.objects.all() # Retrieve all products from the database.
    serializer = ProductSerializer(products, many=True) # Serialize the list of products.
    return Response(serializer.data) # Return the serialized data as a response. return JsonResponse({'data': serializer.data})  # Alternative way to return JSON data.

@api_view(['GET'])
def product_detail(request, pk):
    # Retrieve a product by its primary key or return a 404 error if not found.
    # product = Product.objects.get(id=pk)  # Direct retrieval without 404 handling.
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)



@api_view(['GET'])  
def order_list(request):
    orders = Order.objects.prefetch_related('items__product')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
'''
