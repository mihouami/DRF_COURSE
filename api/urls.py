from django.urls import path
from .views import (
    ProductInfo,
    ProductListCreate,
    ProductDetail,
    OrderViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', OrderViewSet)

urlpatterns = [
    path("products/", ProductListCreate.as_view()),
    path("products/<int:product_id>/", ProductDetail.as_view()),
    path("product_info/", ProductInfo.as_view()),

]

urlpatterns += router.urls
