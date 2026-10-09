from django.db import models

from django.db.models import Sum
from productos.models import Productos
from ventas.models import DetalleVenta

def obtener_top_productos_vendidos():
    # Consulta ORM combinando Ventas y Productos
    return Productos.objects.annotate(
        total_vendido=Sum('detalleventa__cantidad')
    ).order_by('-total_vendido')[:5]
