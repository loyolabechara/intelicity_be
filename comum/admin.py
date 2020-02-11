from django.contrib import admin
from .models import Categoria_Telefone, Telefone

# Register your models here.

class Categoria_TelefoneAdmin(admin.ModelAdmin):
    list_display = ['descricao','dt_inclusao']
    search_fields = ['descricao']

admin.site.register(Categoria_Telefone, Categoria_TelefoneAdmin)

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['nome', 'numero', 'mensageiro', 'dt_inclusao','dt_inclusao']
    list_filter = ['categoria_telefone']
    search_fields = ['nome']

admin.site.register(Telefone, TelefoneAdmin)
