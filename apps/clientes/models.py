from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    documento = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre




