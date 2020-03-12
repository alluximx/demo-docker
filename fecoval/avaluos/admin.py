from django.contrib import admin
from .models import Cliente, Avaluo, DatosCliente, Mancomunado


class ClienteAdmin(admin.ModelAdmin):
    fields = ['cliente', ]


class AvaluoAdmin(admin.ModelAdmin):
    # fields = ['cliente', 'folio']
    readonly_fields = ['cliente', ]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Avaluo, AvaluoAdmin)
admin.site.register(DatosCliente)
admin.site.register(Mancomunado)
