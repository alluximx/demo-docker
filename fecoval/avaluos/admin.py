from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    fields = ['cliente', ]


admin.site.register(Cliente, ClienteAdmin)
