from rest_framework import viewsets
from .models import reporte_dano,notificacion
from .serializers import NotificacionSerializer, ReporteDanoSerializer
class ReporteDanoViewSet(viewsets.ModelViewSet):
    queryset = reporte_dano.objects.all()
    serializer_class = ReporteDanoSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = notificacion.objects.all()
    serializer_class = NotificacionSerializer

