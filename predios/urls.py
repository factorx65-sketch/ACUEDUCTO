
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PredioViewSet,
    MedidorViewSet,
    LecturaViewSet
)

router = DefaultRouter()

router.register('predios', PredioViewSet)
router.register('medidores', MedidorViewSet)
router.register('lecturas', LecturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

