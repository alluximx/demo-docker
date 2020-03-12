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
        avaluo = Avaluo(cliente=validated_data.get('cliente'))
        datos_cliente = validated_data.get('datos_cliente')
        mancomunado = validated_data.get('mancomunado')
        datos_cliente_obj = DatosCliente.objects.create(**datos_cliente)
        mancomunado_obj = Mancomunado.objects.create(**mancomunado)
        avaluo.datos_cliente = datos_cliente_obj
        avaluo.mancomunado = mancomunado_obj
        avaluo.save()
        return validated_data
