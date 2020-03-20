from rest_framework import serializers
from .models import Cliente, Avaluo, DatosCliente, Mancomunado, Estado, Municipio, \
    ADR, ALR, Bien, Proposito, Servicio, Inmueble


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class DatosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCliente
        fields = '__all__'


class MancomunadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mancomunado
        fields = '__all__'


class ALRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALR
        fields = '__all__'


class ADRSerializer(serializers.ModelSerializer):
    alr = ALRSerializer(many=True, read_only=True)

    class Meta:
        model = ADR
        fields = ('id', 'nombre', 'titular', 'localizacion', 'domicilio', 'alr')


class BienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bien
        fields = '__all__'


class PropositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposito
        fields = '__all__'


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'


class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = '__all__'


class AvaluoSerializer(serializers.ModelSerializer):
    cliente_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cliente.objects.all(), source='cliente')
    cliente = ClienteSerializer(read_only=True)
    bien_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Bien.objects.all(), source='tipo_bien')
    tipo_bien = BienSerializer(read_only=True)
    datos_cliente = DatosClienteSerializer()
    mancomunado = MancomunadoSerializer()
    fecha_asignacion = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'], required=False)
    fecha_compromiso = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'], required=False)
    fecha_solicitud_correo = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'], required=False)

    class Meta:
        model = Avaluo
        exclude = ()

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
