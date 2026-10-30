from rest_framework import viewsets

from .models import tarifa, factura, pago

from .serializers import TarifaSerializers, FacturaSerializers, PagoSerializers



class TarifaViewSet(viewsets.ModelViewSet):
    queryset = tarifa.objects.all()
    serializer_class = TarifaSerializers


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = factura.objects.all()
    serializer_class = FacturaSerializers


class PagoViewSet(viewsets.ModelViewSet):
    queryset = pago.objects.all()
    serializer_class = PagoSerializers




# Create your views here.
