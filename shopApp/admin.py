from django.contrib import admin

# Register your models here.

from .models import Product,Customer,Order, OrderDetail, Category, Image

class ProductInline(admin.TabularInline):
    model = OrderDetail
    extra = 0
    
    def product_name(self, instance):
        return instance.product.name

    readonly_fields = ['product_name']
    fields = ('product_name', 'quantity')
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    readonly_fields=['customer', 'total']
    list_display = ('id', 'date', 'customer_id', 'total')

class CategoryAdmin(admin.ModelAdmin):
    fields = [('name', 'parent')]
    list_display = ('name',)
    

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    
    fields = ('url',)

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    fields = ('name', 'category', 'price', 'stock', 'description')
    list_display = ('name', 'price', 'stock', 'category')
    list_editable = ('price', 'stock')
    list_display_links = ('name', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Image)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)