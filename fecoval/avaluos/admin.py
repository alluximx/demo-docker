from django.contrib import admin
from .models import Cliente, Avaluo


class ClienteAdmin(admin.ModelAdmin):
    fields = ['cliente', ]


class AvaluoAdmin(admin.ModelAdmin):
    # fields = ['cliente', 'folio']
    readonly_fields = ['cliente', ]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Avaluo, AvaluoAdmin)
