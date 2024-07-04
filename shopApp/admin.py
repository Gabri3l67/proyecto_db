from django.contrib import admin

# Register your models here.

from .models import Product,Customer,Order, OrderDetail


class ProductAdmin(admin.ModelAdmin):
    fields = [('name', 'price', 'stock', 'image_url', 'description')]
    list_display = ('name', 'description','image_url', 'price', 'stock')
    list_editable = ('price', 'stock')
    list_display_links = ('name', 'image_url')
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'customer_id', 'total')


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)