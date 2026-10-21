from django.db import models

# Create your models here.

class usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    fecha_registro = models.DateField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres