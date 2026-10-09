from django.db import models

class Almacen(models.Model):
    nombre = models.CharField(max_length=100) # Ej: Bodega Central, Sede Norte
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre



