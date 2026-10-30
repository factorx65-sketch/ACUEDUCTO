from rest_framework import serializers
from .models import usuario

class Usuarioserializers(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = [ 'id', 'nombres', 'apellidos', 'documento', 'telefono', 'correo', 'direccion', 'fecha_registro', 'estado' ]