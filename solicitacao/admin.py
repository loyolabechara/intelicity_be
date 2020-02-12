from django.contrib import admin
from .models import AssuntoSolicitacao, Situacao, Solicitacao

# Register your models here.

class AssuntoSolicitacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao','dt_inclusao']
    search_fields = ['descricao']

admin.site.register(AssuntoSolicitacao, AssuntoSolicitacaoAdmin)

class SituacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao','dt_inclusao']
    search_fields = ['descricao']

admin.site.register(Situacao, SituacaoAdmin)

class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ['assuntosolicitacao', 'descricao', 'user', 'dt_inclusao']
    list_filter = ['assuntosolicitacao']
    search_fields = ['descricao']

admin.site.register(Solicitacao, SolicitacaoAdmin)
