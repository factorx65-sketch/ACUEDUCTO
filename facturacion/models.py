from django.db import models

# Create your models here.
from usuarios.models import usuario
from predios.models import lectura


class tarifa(models.Model):
    nombre_tarifa = models.CharField(max_length=100)

    cargo_fijo = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    valor_m3 = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_tarifa


class factura(models.Model):
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()

    consumo_m3 = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    valor_total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    estado = models.CharField(max_length=20)

    usuario_id = models.ForeignKey(
        usuario,
        on_delete=models.CASCADE
    )

    lectura_id = models.OneToOneField(
        lectura,
        on_delete=models.CASCADE
    )

    tarifa_id = models.ForeignKey(
        tarifa,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)


class pago(models.Model):
    fecha_pago = models.DateField()

    valor_pagado = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    metodo_pago = models.CharField(max_length=30)
    numero_comprobante = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=255)

    factura_id = models.ForeignKey(
        factura,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)