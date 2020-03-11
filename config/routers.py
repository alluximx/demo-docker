from rest_framework import routers
from fecoval.avaluos.viewsets import ClienteViewSet

router = routers.DefaultRouter()

router.register(r'cliente', ClienteViewSet)
