from .models import Historico_Alerta, Responsavel, Alerta, Ponto_Apoio, Dirigente
from django.contrib.auth.models import User, Group

from rest_framework import serializers


class ResponsavelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responsavel
        fields = ['nome', 'celular', 'user', 'dt_inclusao']

class SituacaoSerializer(serializers.ModelSerializer):
    alerta_name = serializers.CharField(source='alerta', read_only=True)
    user_name = serializers.CharField(source='user', read_only=True)
    class Meta:
        model = Historico_Alerta
        fields = ['alerta', 'alerta_name', 'user_name', 'dt_inclusao']

"""
class DirigenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dirigente
        fields = '__all__'
"""

class PontoApoioSerializer(serializers.ModelSerializer):
#    bairro_nome = serializers.CharField(source='bairro', read_only=True)
#    dirigente_nome = DirigenteSerializer(read_only=True, many=True)
#    user_name = serializers.CharField(source='user', read_only=True)
    class Meta:
        model = Ponto_Apoio
        depth=1
        fields = ['id', 'nome', 'diretor', 'dirigente', 'responsavel', 'celular', 'email', 'endereco', 'numero', 'complemento', 'bairro', 'capacidade', 'latitude', 'longitude']
