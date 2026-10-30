
from rest_framework import viewsets
from .models import usuario
from .serializers import Usuarioserializers


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = Usuarioserializers



# Create your views here.
