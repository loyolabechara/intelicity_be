from django.contrib import admin
from .models import Escolaridade, Cargo, Vaga

# Register your models here.

class EscolaridadeAdmin(admin.ModelAdmin):
    list_display = ['descricao','dt_inclusao']
    search_fields = ['descricao']

admin.site.register(Escolaridade, EscolaridadeAdmin)

class CargoAdmin(admin.ModelAdmin):
    list_display = ['nome','dt_inclusao']
    search_fields = ['nome']

admin.site.register(Cargo, CargoAdmin)

class VagaAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'sexo', 'experiencia', 'escolaridade', 'dt_fim','dt_inclusao']
    list_filter = ['escolaridade']
    search_fields = ['cargo']

admin.site.register(Vaga, VagaAdmin)
