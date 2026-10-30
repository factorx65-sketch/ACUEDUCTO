from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('usuarios.urls')),
    path('api/', include('predios.urls')),
    path('api/', include('personal.urls')),
    path('api/', include('facturacion.urls')),
    path('api/', include('comunicaciones.urls')),
]