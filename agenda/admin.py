from django.contrib import admin
from .models import Assunto, Evento

# Register your models here.

class AssuntoAdmin(admin.ModelAdmin):
    list_display = ['descricao','dt_inclusao']
    search_fields = ['descricao']

admin.site.register(Assunto, AssuntoAdmin)

class EventoAdmin(admin.ModelAdmin):
    list_display = ['assunto', 'descricao', 'user', 'dt_evento','dt_inclusao']
    list_filter = ['assunto']
    search_fields = ['descricao']

admin.site.register(Evento, EventoAdmin)
