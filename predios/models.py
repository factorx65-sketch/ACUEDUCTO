from django.db import models

# Create your models here.
from usuarios.models import usuario


class predio(models.Model):
    nombre_predio = models.CharField(max_length=100)
    vereda = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    tipo_predio = models.CharField(max_length=30)
    estado_servicio = models.CharField(max_length=20)

    usuario_id = models.ForeignKey(
        usuario,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre_predio


class medidor(models.Model):
    numero_medidor = models.CharField(max_length=30, unique=True)
    fecha_instalacion = models.DateField()
    estado = models.CharField(max_length=20)
    observaciones = models.CharField(max_length=255)

    predio_id = models.ForeignKey(
        predio,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.numero_medidor


class lectura(models.Model):
    fecha_lectura = models.DateField()

    lectura_anterior = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    lectura_actual = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    consumo_m3 = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    observaciones = models.CharField(max_length=255)

    medidor_id = models.ForeignKey(
        medidor,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)