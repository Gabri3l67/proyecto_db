from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=16,decimal_places=2)
    image_url = models.TextField(max_length=1024, null=True)
    stock = models.IntegerField(db_default=0)


class ShoppingCart(models.Model):
    session_id = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    product_id = models.CharField(max_length=255, null=False)  # Assuming product_id is a string
    amount = models.IntegerField(default=0)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255, null=False) 
    last_name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255)

# Pedido
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    total = models.DecimalField(max_digits=16, decimal_places=2, default=0)

#PedidoDetalle
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    quantity = models.IntegerField(default=0)


# class Auditoria(models.Model):
#     pass