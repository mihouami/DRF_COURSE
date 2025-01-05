from django.contrib import admin
from api.models import OrderItem, Order, User


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    
admin.site.register(User)