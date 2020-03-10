from django.db import models


class Cliente(models.Model):
    cliente = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.cliente


class DatosCliente(models.Model):
    PERSONA_CHOICES = (
        ('F', 'Persona Física'),
        ('M', 'Persona Moral'),
    )
    persona = models.CharField(choices=PERSONA_CHOICES, null=True, max_length=255)
    nombre = models.CharField(null=True, max_length=255)
    apellido_paterno = models.CharField(null=True, max_length=255)
    apellido_materno = models.CharField(null=True, max_length=255)
    rfc = models.CharField(null=True, max_length=255)
    curp = models.CharField(null=True, max_length=255)
    nss = models.CharField(null=True, max_length=255)
    telefono = models.CharField(null=True, max_length=255)


class Mancomunado(models.Model):
    nombre = models.CharField(null=True, max_length=255)
    rfc = models.CharField(null=True, max_length=255)
    telefono = models.CharField(null=True, max_length=255)
    celular = models.CharField(null=True, max_length=255)


class Estado(models.Model):
    clave = models.CharField(null=True, max_length=255)
    nombre = models.CharField(null=False, max_length=255)
    abrev = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __unicode__(self):
        if self.nombre is None:
            return "N/D"
        else:
            return self.nombre


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    clave = models.CharField(null=True, max_length=255)
    nombre = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __unicode__(self):
        if self.nombre is None:
            return "N/D"
        else:
            return self.nombre


class Localidad(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    clave = models.CharField(null=True, max_length=255)
    nombre = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __unicode__(self):
        if self.nombre is None:
            return "N/D"
        else:
            return self.nombre


class ADR(models.Model):
    nombre = models.CharField(null=False, max_length=255)


class Avaluo(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    datos_cliente = models.ForeignKey(DatosCliente, null=True, on_delete=models.CASCADE)
    mancomunado = models.OneToOneField(Mancomunado, null=True, on_delete=models.CASCADE)
    folio = models.CharField(null=True, max_length=255)
    fecha_asignacion = models.DateField(null=True)
    fecha_compromiso = models.DateField(null=True)
    fecha_solicitud_correo = models.DateField(null=True)
    credito_fiscal = models.CharField(null=True, max_length=255)
    codigo_postal = models.CharField(null=True, max_length=255)
    calle = models.CharField(null=True, max_length=255)
    no_ext = models.CharField(null=True, max_length=255)
    no_int = models.CharField(null=True, max_length=255)
    colonia = models.CharField(null=True, max_length=255)
    lote = models.CharField(null=True, max_length=255)
    manzana = models.CharField(null=True, max_length=255)
    estado = models.ForeignKey(Estado, null=True, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, null=True, on_delete=models.CASCADE)
    localidad = models.CharField(null=True, max_length=255)
    titular_adr = models.ForeignKey(ADR, null=True, on_delete=models.CASCADE)
    localizacion_adr = models.CharField(null=True, max_length=255)
    domicilio_adr = models.CharField(null=True, max_length=255)
    alr = models.CharField(null=True, max_length=255)
