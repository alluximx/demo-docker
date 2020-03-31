from rest_framework import routers
from fecoval.avaluos.viewsets import ClienteViewSet, AvaluoViewSet, EstadoViewSet, ADRViewSet, BienViewSet, \
    PropositoViewSet, ServicioViewSet, InmuebleViewSet, ColegioViewSet, ValuadorViewSet, PropuestaTecnicaViewSet


router = routers.DefaultRouter()

router.register(r'cliente', ClienteViewSet)
router.register(r'avaluo', AvaluoViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'bien', BienViewSet)
router.register(r'proposito', PropositoViewSet)
router.register(r'adr', ADRViewSet)
router.register(r'servicio', ServicioViewSet)
router.register(r'colegios', ColegioViewSet)
router.register(r'valuadores', ValuadorViewSet)
router.register(r'propuestas_tecnicas', PropuestaTecnicaViewSet)
router.register(r'inmueble', InmuebleViewSet)
