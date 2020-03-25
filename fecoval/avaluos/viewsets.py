from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cliente, Avaluo, Estado, Municipio, ADR, Bien, Proposito, Servicio, Inmueble
from .serializers import ClienteSerializer, AvaluoSerializer, EstadoSerializer, MunicipioSerializer, \
    ADRSerializer, BienSerializer, PropositoSerializer, ServicioSerializer, InmuebleSerializer


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ADRViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ADR.objects.all()
    serializer_class = ADRSerializer


class AvaluoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Avaluo.objects.all().order_by('-id')
    serializer_class = AvaluoSerializer


class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Estado.objects.all().order_by('nombre')
    serializer_class = EstadoSerializer

    @action(detail=True)
    def municipios(self, request, pk=None):
        estado = self.get_object()
        municipios = Municipio.objects.filter(estado=estado).order_by('nombre')
        municipios_json = MunicipioSerializer(municipios, many=True)
        return Response(municipios_json.data)


class BienViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Bien.objects.all().order_by('id')
    serializer_class = BienSerializer


class PropositoViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Proposito.objects.all()
    serializer_class = PropositoSerializer


class ServicioViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class InmuebleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer
