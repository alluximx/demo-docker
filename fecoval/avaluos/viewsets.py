from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cliente, Avaluo, Estado, Municipio, ADR, Bien, Proposito, Servicio, Colegio, Valuador, \
    PropuestaTecnica
from .serializers import ClienteSerializer, AvaluoSerializer, EstadoSerializer, MunicipioSerializer, \
    ADRSerializer, BienSerializer, PropositoSerializer, ServicioSerializer, InmuebleSerializer, ColegioSerializer, \
    ValuadorSerializer, PropuestaTecnicaSerializer


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


class ColegioViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Colegio.objects.filter(estatus=True)
    serializer_class = ColegioSerializer

    @action(detail=True)
    def presidente(self, request, pk=None):
        colegio = self.get_object()
        return Response(colegio.presidente.first_name + ' ' + colegio.presidente.last_name)


class ValuadorViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Valuador.objects.filter(estatus=True)
    serializer_class = ValuadorSerializer


class PropuestaTecnicaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PropuestaTecnica.objects.all()
    serializer_class = PropuestaTecnicaSerializer
