from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Custom user model extending Django's built-in AbstractUser.
class User(AbstractUser):
    pass

# Product model to represent items available for purchase.
class Product(models.Model):
    name = models.CharField(max_length=255)  # Name of the product.
    description = models.TextField()  # Detailed description of the product.
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product with up to 2 decimal places.
    stock = models.PositiveIntegerField()  # Quantity of the product available in stock.
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Optional image of the product.
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the product was created.
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the product was last updated.

    @property
    def in_stock(self):
        # Property to check if the product is in stock.
        return self.stock > 0

    def __str__(self):
        # String representation of the product, used in admin and debugging.
        return self.name

# Order model to represent customer orders.
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        # Possible statuses for an order.
        PENDING = 'Pending'
        COMPLETED = 'Confirmed'
        CANCELLED = 'Cancelled'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)  # Unique identifier for each order.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who placed the order.
    products = models.ManyToManyField(
        Product, through='OrderItem', related_name='orders'
    )  # Many-to-many relationship with products via the OrderItem model.
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the order was created.
    status = models.CharField(
        max_length=255, choices=StatusChoices.choices, default=StatusChoices.PENDING
    )  # Current status of the order.

    def __str__(self):
        # String representation of the order.
        return f'Order {self.order_id} by {self.user.username}'

# OrderItem model to represent the relationship between orders and products.
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items'
    )  # The order this item belongs to.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # The product in this order item.
    quantity = models.PositiveIntegerField()  # Quantity of the product in this order.

    @property
    def item_subtotal(self):
        # Property to calculate the subtotal cost of this item (price * quantity).
        return self.product.price * self.quantity

    def __str__(self):
        # String representation of the order item.
        return f'{self.product.name} x {self.quantity} in order {self.order.order_id}'
