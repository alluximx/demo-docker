from django.db import models


class Cliente(models.Model):
    cliente = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.cliente


class Estado(models.Model):
    clave = models.CharField(null=True, max_length=255)
    nombre = models.CharField(null=False, max_length=255)
    abrev = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __str__(self):
        if self.nombre is None:
            return "N/D"
        else:
            return self.nombre


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    clave = models.CharField(null=True, max_length=255)
    nombre = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __str__(self):
        if self.nombre is None:
            return "N/D"
        else:
            return self.nombre


class Localidad(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    clave = models.CharField(null=True, max_length=255)
    nombre = models.CharField(null=False, max_length=255)
    is_active = models.BooleanField(null=False, default=1)

    def __str__(self):
        if self.nombre is None:
            return "N/D"
        else:
            return self.nombre


class ADR(models.Model):
    nombre = models.CharField(null=False, max_length=255)


class Avaluo(models.Model):
    LOCALIZADO_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    folio = models.CharField(blank=True, null=True, max_length=255)
    fecha_asignacion = models.DateField(blank=True, null=True)
    fecha_compromiso = models.DateField(blank=True, null=True)
    fecha_solicitud_correo = models.DateField(blank=True, null=True)
    credito_fiscal = models.CharField(blank=True, null=True, max_length=255)
    codigo_postal = models.CharField(blank=True, null=True, max_length=255)
    calle = models.CharField(blank=True, null=True, max_length=255)
    no_ext = models.CharField(blank=True, null=True, max_length=255)
    no_int = models.CharField(blank=True, null=True, max_length=255)
    colonia = models.CharField(blank=True, null=True, max_length=255)
    lote = models.CharField(blank=True, null=True, max_length=255)
    manzana = models.CharField(blank=True, null=True, max_length=255)
    estado = models.ForeignKey(Estado, blank=True, null=True, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, blank=True, null=True, on_delete=models.CASCADE)
    localidad = models.CharField(blank=True, null=True, max_length=255)
    localizado = models.CharField(blank=True, null=True, choices=LOCALIZADO_CHOICES, max_length=35)
    titular_adr = models.ForeignKey(ADR, blank=True, null=True, on_delete=models.CASCADE)
    localizacion_adr = models.CharField(blank=True, null=True, max_length=255)
    domicilio_adr = models.CharField(blank=True, null=True, max_length=255)
    alr = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return str(self.pk)


class DatosCliente(models.Model):
    PERSONA_CHOICES = (
        ('F', 'Persona Física'),
        ('M', 'Persona Moral'),
    )
    avaluo = models.OneToOneField(Avaluo, null=True, on_delete=models.CASCADE, related_name="datos_cliente")
    persona = models.CharField(choices=PERSONA_CHOICES, blank=True, null=True, max_length=255)
    nombre = models.CharField(blank=True, null=True, max_length=255)
    apellido_paterno = models.CharField(blank=True, null=True, max_length=255)
    apellido_materno = models.CharField(blank=True, null=True, max_length=255)
    rfc = models.CharField(blank=True, null=True, max_length=255)
    curp = models.CharField(blank=True, null=True, max_length=255)
    nss = models.CharField(blank=True, null=True, max_length=255)
    telefono = models.CharField(blank=True, null=True, max_length=255)


class Mancomunado(models.Model):
    avaluo = models.OneToOneField(Avaluo, null=True, on_delete=models.CASCADE, related_name="mancomunado")
    nombre = models.CharField(blank=True, null=True, max_length=255)
    rfc = models.CharField(blank=True, null=True, max_length=255)
    telefono = models.CharField(blank=True, null=True, max_length=255)
    celular = models.CharField(blank=True, null=True, max_length=255)
