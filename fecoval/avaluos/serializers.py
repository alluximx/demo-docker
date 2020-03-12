from rest_framework import serializers
from .models import Cliente, Avaluo, DatosCliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class DatosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCliente
        fields = '__all__'


class AvaluoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    datos_cliente = DatosClienteSerializer()

    class Meta:
        model = Avaluo
        # fields = '__all__'
        fields = ('cliente', 'datos_cliente')

    def create(self, validated_data):
        avaluo = Avaluo(cliente=validated_data.get('cliente'))
        datos_cliente = validated_data.get('datos_cliente')
        datos_cliente_obj = DatosCliente.objects.create(**datos_cliente)
        avaluo.datos_cliente = datos_cliente_obj
        avaluo.save()
        return validated_data
