from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Avaluo
from .serializers import ClienteSerializer, AvaluoSerializer


class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class AvaluoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Avaluo.objects.all()
    serializer_class = AvaluoSerializer
