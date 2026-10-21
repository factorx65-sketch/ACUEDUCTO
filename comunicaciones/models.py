from django.db import models

# Create your models here.
from usuarios.models import usuario
from personal.models import empleado


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