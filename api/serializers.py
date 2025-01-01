from rest_framework import serializers  # Importing serializers from DRF to define API representations.
from .models import User, Product, Order, OrderItem  # Importing models for serialization.

####### PRODUCTS SERIALIZER #######
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # Specifies the model this serializer is based on.
        fields = (
            'id',  # Unique identifier for the product.
            'name',  # Name of the product.
            # 'description',  # Uncomment if you want to include product descriptions in the API response.
            'price',  # Price of the product.
            'stock',  # Quantity of the product available in stock.
        )
        read_only_fields = ('id',)  # The 'id' field is read-only and cannot be modified.
        # write_only_fields = ('price',)  # Uncomment if you want to allow price to be write-only.

    def validate_price(self, value):
        # Custom validation to ensure the price is greater than zero.
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than zero.')
        return value

####### ORDER ITEM SERIALIZER #######
class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()  # Uncomment to include nested product details.
    product_name = serializers.CharField(source='product.name')  # Retrieves the name of the associated product.
    product_price = serializers.DecimalField(
        source='product.price', max_digits=10, decimal_places=2
    )  # Retrieves the price of the associated product.

    class Meta:
        model = OrderItem  # Specifies the model this serializer is based on.
        fields = (
            'product_name',  # Name of the product.
            'product_price',  # Price of the product.
            'quantity',  # Quantity of the product in the order.
            'item_subtotal',  # Subtotal for the item (price * quantity).
            # 'order'  # Uncomment if you need to include order details in the API response.
        )

####### ORDER SERIALIZER #######
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Nested representation of order items.
    total_price = serializers.SerializerMethodField()  # Calculates the total price of the order.

    class Meta:
        model = Order  # Specifies the model this serializer is based on.
        fields = (
            'order_id',  # Unique identifier for the order.
            'created_at',  # Timestamp when the order was created.
            'user',  # User who placed the order.
            'status',  # Current status of the order.
            'items',  # List of items in the order.
            'total_price',  # Total price of all items in the order.
        )

    def get_total_price(self, obj):
        # Custom method to calculate the total price of the order.
        order_items = obj.items.all()  # Retrieve all items in the order.
        return sum(order_item.item_subtotal for order_item in order_items)  # Sum the subtotals of all items.


class ProductInfoSerializer(serializers.Serializer):
    #Get all products, count of products and max price of products
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
    total_stock_value = serializers.FloatField()