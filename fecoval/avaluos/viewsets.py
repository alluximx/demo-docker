from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cliente, Avaluo, Estado, Municipio, ADR
from .serializers import ClienteSerializer, AvaluoSerializer, EstadoSerializer, MunicipioSerializer, ADRSerializer


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
