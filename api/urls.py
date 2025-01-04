from django.urls import path
from .views import (
    ProductInfo,
    ProductListCreate,
    ProductDetail,
    OrderList,
    UserOrderList,
)

urlpatterns = [
    path("products/", ProductListCreate.as_view()),
    path("products/<int:product_id>/", ProductDetail.as_view()),
    path("product_info/", ProductInfo.as_view()),
    path("orders/", OrderList.as_view()),
    path("user-orders/", UserOrderList.as_view(), name="user-orders"),
    
]
