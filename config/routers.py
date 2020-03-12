from rest_framework import routers
from fecoval.avaluos.viewsets import ClienteViewSet, AvaluoViewSet

router = routers.DefaultRouter()

router.register(r'cliente', ClienteViewSet)
router.register(r'avaluo', AvaluoViewSet)
