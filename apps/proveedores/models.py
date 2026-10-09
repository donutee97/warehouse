from django.db import models

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=150)
    nit_rut = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.razon_social


