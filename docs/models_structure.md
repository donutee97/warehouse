# Esquema de Modelos y Relaciones (models.py por App)

## App: categorias
(No depende de ninguna otra app)
```
# categorias/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
```

## App: proveedores
(No depende de ninguna otra app)
```
# proveedores/models.py
from django.db import models

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=150)
    nit_rut = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.razon_social
```

## App: clientes
(No depende de ninguna otra app)
```
# clientes/models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    documento = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
```

## App: almacenes
(No depende de ninguna otra app)
```
# almacenes/models.py
from django.db import models

class Almacen(models.Model):
    nombre = models.CharField(max_length=100) # Ej: Bodega Central, Sede Norte
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
```

## App: productos
(Se conecta con categorias y proveedores)
```
# productos/models.py
from django.db import models
from categorias.models import Categoria, Marca
from proveedores.models import Proveedor

class Producto(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Relaciones
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    proveedores = models.ManyToManyField(Proveedor, related_name='productos_ofrecidos')

    def __str__(self):
        return f"{self.sku} - {self.nombre}"
```

## App: compras
(Registra entradas al inventario; conecta proveedores, almacenes y productos)
```
# compras/models.py
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
```

## App: ventas
(Registra salidas de mercancía; conecta clientes, almacenes y productos)
```
# ventas/models.py
from django.db import models
from clientes.models import Cliente
from almacenes.models import Almacen
from productos.models import Producto

class OrdenVenta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    almacen_origen = models.ForeignKey(Almacen, on_delete=models.PROTECT)

class DetalleVenta(models.Model):
    orden = models.ForeignKey(OrdenVenta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
```

## App: movimientos
(Gestiona traslados entre bodegas y stock físico real por almacén)
```
# movimientos/models.py
from django.db import models
from productos.models import Producto
from almacenes.models import Almacen

class InventarioStock(models.Model):
    """
    Control de existencias físicas por almacén y producto
    """
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
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
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
```

## App: reportes
(No crea tablas nuevas obligatoriamente; consume el ORM de las demás apps para hacer consultas complejas)
```
# reportes/views.py (Ejemplo de uso del ORM)
from django.db.models import Sum
from productos.models import Producto
from ventas.models import DetalleVenta

def obtener_top_productos_vendidos():
    # Consulta ORM combinando Ventas y Productos
    return Producto.objects.annotate(
        total_vendido=Sum('detalleventa__cantidad')
    ).order_by('-total_vendido')[:5]
```