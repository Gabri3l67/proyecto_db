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
    product_id = models.CharField(max_length=255, null=False)  # Assuming product_id is a string
    amount = models.IntegerField(default=0)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255, null=False) 
    last_name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255)

# class Pedido(models.Model):
#     pass

# class PedidoDetalle(models.Model):
#     pass

# class Auditoria(models.Model):
#     pass