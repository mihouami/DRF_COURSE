from .serializers import (
    ProductSerializer,
    OrderSerializer,
    ProductInfoSerializer,
)
from .models import Product, Order
from django.db.models import Max
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


##### PRODUCTS VIEWS #####
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

##### PRODUCT DETAIL VIEW #####
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"


##### ORDERS VIEWS #####
class OrderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items__product")
    serializer_class = OrderSerializer


##### USER ORDER LIST VIEW #####
class UserOrderList(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items__product")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)


##### PRODUCT INFO VIEWS #####
class ProductInfo(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer(
            {
                "products": products,
                "count": len(products),
                "max_price": products.aggregate(max_price=Max("price"))["max_price"],
                "total_stock_value": sum(p.price * p.stock for p in products),
            }
        )
        return Response(serializer.data)
