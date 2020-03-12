from rest_framework import serializers
from .models import Cliente, Avaluo, DatosCliente, Mancomunado


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class DatosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCliente
        fields = '__all__'


class MancomunadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mancomunado
        fields = '__all__'


class AvaluoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    datos_cliente = DatosClienteSerializer()
    mancomunado = MancomunadoSerializer()

    class Meta:
        model = Avaluo
        fields = '__all__'
        # fields = ['cliente', 'datos_cliente', 'mancomunado']

    def create(self, validated_data):
        datos_cliente_data = validated_data.pop('datos_cliente', None)
        mancomunado_data = validated_data.pop('mancomunado', None)

        avaluo = Avaluo.objects.create(**validated_data)

        if datos_cliente_data:
            datos_cliente = DatosCliente.objects.create(avaluo=avaluo, **datos_cliente_data)
            validated_data['datos_cliente'] = datos_cliente
        if mancomunado_data:
            mancomunado = Mancomunado.objects.create(avaluo=avaluo, **mancomunado_data)
            validated_data['mancomunado'] = mancomunado

        return validated_data
