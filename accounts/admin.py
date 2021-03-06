from django.contrib import admin
from .models import Usuario, Estado, Cidade, Bairro

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['user','cpf','celular', 'bairro', 'dt_nascimento', 'dt_inclusao']
    list_filter = ['bairro']
    search_fields = ['user_name', 'cpf', 'celular']

admin.site.register(Usuario, UsuarioAdmin)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

admin.site.register(Estado, EstadoAdmin)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ['estado', 'nome']
    list_filter = ['estado']
    search_fields = ['nome']

admin.site.register(Cidade, CidadeAdmin)

class BairroAdmin(admin.ModelAdmin):
    list_display = ['cidade', 'nome']
    list_filter = ['cidade']
    search_fields = ['nome']

admin.site.register(Bairro, BairroAdmin)
