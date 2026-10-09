from django.db import models
from apps.proveedores.models import Proveedor
from apps.categorias.models import Categorias, Marca

class Productos(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.ForeignKey(Categorias, on_delete=models.PROTECT, related_name='productos')
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    proveedores = models.ManyToManyField(Proveedor, related_name='productos_ofrecidos')

    def __str__(self):
        return f"{self.sku} - {self.nombre}"
