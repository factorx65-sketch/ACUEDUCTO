from django.db import models

# Create your models here.
class empleado(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres