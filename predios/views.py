
from rest_framework import viewsets

from .models import predio, medidor, lectura

from .serializers import (
    PredioSerializers,
    MedidorSerializers,
    LecturaSerializers
)


class PredioViewSet(viewsets.ModelViewSet):
    queryset = predio.objects.all()
    serializer_class = PredioSerializers


class MedidorViewSet(viewsets.ModelViewSet):
    queryset = medidor.objects.all()
    serializer_class = MedidorSerializers


class LecturaViewSet(viewsets.ModelViewSet):
    queryset = lectura.objects.all()
    serializer_class = LecturaSerializers



# Create your views here.
