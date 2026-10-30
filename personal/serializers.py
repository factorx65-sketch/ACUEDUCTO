from rest_framework import serializers
from .models import empleado


class EmpleadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = [
            'id',
            'nombres',
            'apellidos',
            'documento',
            'telefono',
            'cargo',
            'fecha_contratacion',
            'estado'
        ]

