from django.contrib import admin
from .models import Cliente, Avaluo, DatosCliente, Mancomunado, ADR, ALR, Bien, Proposito, Servicio, Inmueble, Empresa, \
    Colegio, Valuador, ColegioAvaluo, PropuestaTecnica, Estado, Municipio


class ClienteAdmin(admin.ModelAdmin):
    fields = ['nombre', ]


class AvaluoAdmin(admin.ModelAdmin):
    # fields = ['cliente', 'folio']
    readonly_fields = ['cliente', ]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Avaluo, AvaluoAdmin)
admin.site.register(DatosCliente)
admin.site.register(Mancomunado)
admin.site.register(ADR)
admin.site.register(ALR)
admin.site.register(Bien)
admin.site.register(Proposito)
admin.site.register(Servicio)
admin.site.register(Inmueble)
admin.site.register(Empresa)
admin.site.register(Colegio)
admin.site.register(Valuador)
admin.site.register(ColegioAvaluo)
admin.site.register(PropuestaTecnica)
admin.site.register(Estado)
admin.site.register(Municipio)
