from django.db import models


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


class reporte_dano(models.Model):
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    tipo_dano = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=150)
    estado = models.CharField(max_length=30)
    fecha_solucion = models.DateField(null=True, blank=True)

    usuario_id = models.ForeignKey(
        usuario,
        on_delete=models.CASCADE
    )

    empleado_id = models.ForeignKey(
        empleado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.id)


class notificacion(models.Model):
    fecha_envio = models.DateTimeField(auto_now_add=True)
    tipo_notificacion = models.CharField(max_length=50)
    mensaje = models.TextField()
    medio = models.CharField(max_length=30)
    estado = models.CharField(max_length=20)

    usuario_id = models.ForeignKey(
        usuario,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)




