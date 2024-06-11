from django.contrib import admin
from .models import Product, Order, Cart, Notification, Support

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'format', 'sides', 'colored', 'paper_type', 'price_per_unit', 'available')
    list_filter = ('format', 'sides')
    ordering = ('product_name',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('product_name',),
        }
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'format', 'sides', 'colored', 'paper_type', 'extra_info', 'file', 'amount', 'cost')
    list_filter = ('format', 'sides')
    ordering = ('order_id',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'format', 'colored', 'sides', 'paper_type', 'extra_info', 'file', 'amount', 'cost')
    list_filter = ('format', 'sides')
    ordering = ('user',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    ordering = ('name', 'email')

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'message')
    ordering = ('name', 'surname', 'email')