from django.contrib import admin
from .models import Dirigente, Responsavel, Ponto_Apoio, Alerta,Historico_Alerta

# Register your models here.

from .models import Dirigente
admin.site.register(Dirigente)

from .models import Responsavel
admin.site.register(Responsavel)

class Ponto_ApoioAdmin(admin.ModelAdmin):
    list_display = ['nome','diretor', 'bairro', 'dt_inclusao']
    list_filter = ['bairro']
    search_fields = ['user_name', 'cpf', 'celular']

admin.site.register(Ponto_Apoio, Ponto_ApoioAdmin)


from .models import Alerta
admin.site.register(Alerta)

class Historico_AlertaAdmin(admin.ModelAdmin):
    list_display = ['alerta', 'user', 'dt_inclusao']
#    list_filter = ['bairro']
    search_fields = ['alerta', 'dt_inclusao']

admin.site.register(Historico_Alerta, Historico_AlertaAdmin)
