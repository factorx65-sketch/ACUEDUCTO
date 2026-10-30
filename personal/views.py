
from rest_framework import viewsets
from .models import empleado
from .serializers import EmpleadoSerializers


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = empleado.objects.all()
    serializer_class = EmpleadoSerializers



# Create your views here.
