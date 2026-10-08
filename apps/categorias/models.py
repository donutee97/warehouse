from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    