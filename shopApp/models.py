from django.db import models

# Create your models here.

class Productos(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=16,decimal_places=2)
    image_url = models.TextField(max_length=1024, null=True)
    stock = models.IntegerField(db_default=0)


class ShoppingCart(models.Model):
    session_id = models.CharField(max_length=255, null=False)
    product_id = models.CharField(max_length=255, null=False)  # Assuming product_id is a string
    amount = models.IntegerField(default=0)

# class Cliente(models.Model):
#     pass

# class Pedido(models.Model):
#     pass

# class PedidoDetalle(models.Model):
#     pass

# class Auditoria(models.Model):
#     pass