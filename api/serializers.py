from rest_framework import serializers
from .models import User, Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            #'description',
            'price',
            'stock',
        )
        read_only_fields = ('order_id',)
        #write_only_fields = ('price',)
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than zero.')
        return value