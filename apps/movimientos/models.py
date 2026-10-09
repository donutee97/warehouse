from django.db import models

from django.db import models
from apps.productos.models import Productos
from apps.almacenes.models import Almacen

class InventarioStock(models.Model):
    """
    Control de existencias físicas por almacén y producto
    """
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    class Meta:
        unique_together = ('producto', 'almacen')

class Transferencia(models.Model):
    """
    Traspaso directo entre 2 almacenes (origen -> destino)
    """
    fecha = models.DateTimeField(auto_now_add=True)
    almacen_origen = models.ForeignKey(Almacen, on_delete=models.PROTECT, related_name='salidas_transferencia')
    almacen_destino = models.ForeignKey(Almacen, on_delete=models.PROTECT, related_name='entradas_transferencia')
    producto = models.ForeignKey(Productos, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
