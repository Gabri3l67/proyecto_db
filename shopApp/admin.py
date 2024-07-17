from django.contrib import admin

# Register your models here.

from .models import Product,Customer,Order, OrderDetail

class ProductInline(admin.TabularInline):
    model = OrderDetail
    extra = 0
    
    def product_name(self, instance):
        return instance.product.name

    readonly_fields = ['product_name']
    fields = ('product_name', 'quantity')

class ProductAdmin(admin.ModelAdmin):
    fields = [('name', 'price', 'stock', 'image_url', 'description')]
    list_display = ('name', 'description','image_url', 'price', 'stock')
    list_editable = ('price', 'stock')
    list_display_links = ('name', 'image_url')
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    readonly_fields=['customer', 'total']
    list_display = ('id', 'date', 'customer_id', 'total')


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)