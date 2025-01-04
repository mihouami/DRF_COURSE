from rest_framework import serializers
from .models import (
    Product,
    Order,
    OrderItem,
)


####### PRODUCTS SERIALIZER #######
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "stock",
        )
        read_only_fields = ("id",)

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value


####### ORDER ITEM SERIALIZER #######
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    product_price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = (
            "product_name",
            "product_price",
            "quantity",
            "item_subtotal",
        )


####### ORDER SERIALIZER #######
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = (serializers.SerializerMethodField())

    class Meta:
        model = Order
        fields = (
            "order_id",
            "created_at",
            "user",
            "status",
            "items",
            "total_price",
        )

    def get_total_price(self, obj):
        order_items = obj.items.all()
        return sum(
            order_item.item_subtotal for order_item in order_items
        )


class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
    total_stock_value = serializers.FloatField()