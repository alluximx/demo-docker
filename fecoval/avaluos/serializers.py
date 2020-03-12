from rest_framework import serializers
from .models import Cliente, Avaluo


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class AvaluoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())

    class Meta:
        model = Avaluo
        # fields = '__all__'
        fields = ('cliente',)
