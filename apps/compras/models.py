from django.db import models

from django.db import models
from proveedores.models import Proveedor
from almacenes.models import Almacen
from productos.models import Producto

class OrdenCompra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    almacen_destino = models.ForeignKey(Almacen, on_delete=models.PROTECT)

class DetalleCompra(models.Model):
    orden = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
