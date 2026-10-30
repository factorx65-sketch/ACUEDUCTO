from rest_framework import serializers
from .models import tarifa, factura, pago 
class TarifaSerializers(serializers.ModelSerializer): 
    class Meta:
        model = tarifa
        fields = [ 'id', 'nombre_tarifa', 'cargo_fijo', 'valor_m3', 'fecha_inicio', 'fecha_fin', 'estado' 
         ]
        
class FacturaSerializers(serializers.ModelSerializer):
    class Meta: 
        model = factura
        fields = [ 'id', 'fecha_emision', 'fecha_vencimiento', 'consumo_m3', 'valor_total', 'estado', 'usuario_id', 'lectura_id', 'tarifa_id' ]
        
class PagoSerializers(serializers.ModelSerializer):
      class Meta: 
        model = pago 
        fields = [ 'id', 'fecha_pago', 'valor_pagado', 'metodo_pago', 'numero_comprobante', 'observaciones', 'factura_id' ] 