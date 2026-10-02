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