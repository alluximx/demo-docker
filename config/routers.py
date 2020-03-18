from rest_framework import routers
from fecoval.avaluos.viewsets import ClienteViewSet, AvaluoViewSet, EstadoViewSet, ADRViewSet

router = routers.DefaultRouter()

router.register(r'cliente', ClienteViewSet)
router.register(r'avaluo', AvaluoViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'adr', ADRViewSet)
