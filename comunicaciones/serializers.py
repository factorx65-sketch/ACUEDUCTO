from rest_framework import serializers
from .models import  reporte_dano, notificacion

class ReporteDanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = reporte_dano
        fields = [ 'id', 'fecha_reporte', 'tipo_dano', 'descripcion', 'ubicacion', 'estado', 'fecha_solucion', 'usuario_id', 'empleado_id' ]
        

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = notificacion
        fields = [ 'id', 'fecha_envio', 'tipo_notificacion', 'mensaje', 'medio', 'estado', 'usuario_id' ]
    
        
          
          
          