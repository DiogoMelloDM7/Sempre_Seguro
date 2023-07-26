from django.contrib import admin
from .models import Conta, Recebimento, FuturasCompra, Relatorio, Usuario, ContasAVencer, ContasInformada
from django.contrib.auth.admin import UserAdmin
# Register your models here.

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Informações", {'fields': ('telefone',)})
)

UserAdmin.fieldsets = tuple(campos)

admin.site.register(Conta)
admin.site.register(Recebimento)
admin.site.register(FuturasCompra)
admin.site.register(Relatorio)
admin.site.register(Usuario, UserAdmin)
admin.site.register(ContasAVencer)
admin.site.register(ContasInformada)
