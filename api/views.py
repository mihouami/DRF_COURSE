from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    #return JsonResponse({'data': serializer.data})
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    #product = Product.objects.get(id=pk)
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
