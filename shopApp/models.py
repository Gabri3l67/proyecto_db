from django.db import models

# Create your models here.

class Productos(models.Model):
    name = models.CharField(max_length=255, null=False)

# class Clientes(models.Model):
#     pass

# class Pedidos(models.Model):
#     pass

# class PedidoDetalles(models.Model):
#     pass

# class Auditoria(models.Model):
#     pass