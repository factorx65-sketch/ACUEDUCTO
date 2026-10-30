from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import ReporteDanoViewSet, NotificacionViewSet

router = DefaultRouter()

router.register(
    'reportedano',
    ReporteDanoViewSet,
    basename='reportedano'
)

router.register(
    'notificacion',
    NotificacionViewSet,
    basename='notificacion'
)

urlpatterns = [
    path('', include(router.urls)),
]