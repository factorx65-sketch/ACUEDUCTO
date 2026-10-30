from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    TarifaViewSet,
    FacturaViewSet,
    PagoViewSet
)

router = DefaultRouter()

router.register('tarifas', TarifaViewSet)
router.register('facturas', FacturaViewSet)
router.register('pagos', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

