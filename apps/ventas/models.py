from django.db import models

from django.db import models
from clientes.models import Cliente
from almacenes.models import Almacen
from productos.models import Productos

class OrdenVenta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    almacen_origen = models.ForeignKey(Almacen, on_delete=models.PROTECT)

class DetalleVenta(models.Model):
    orden = models.ForeignKey(OrdenVenta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Productos, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
