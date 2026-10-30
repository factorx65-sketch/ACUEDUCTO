from rest_framework import serializers
from .models import predio, medidor, lectura

class PredioSerializers(serializers.ModelSerializer):
    class Meta:
        model = predio
        fields = [ 'id', 'nombre_predio', 'vereda', 'direccion', 'tipo_predio', 'estado_servicio', 'usuario_id' ]
        
class MedidorSerializers(serializers.ModelSerializer):
    class Meta:
        model = medidor
        fields =     [ 'id', 'numero_medidor', 'fecha_instalacion', 'estado', 'observaciones', 'predio_id' ] 
        
class LecturaSerializers(serializers.ModelSerializer):
    class Meta:
        model = lectura
        fields =    [ 'id', 'fecha_lectura', 'lectura_anterior', 'lectura_actual', 'consumo_m3', 'observaciones', 'medidor_id' ]       
        
