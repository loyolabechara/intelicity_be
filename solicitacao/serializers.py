from rest_framework import serializers

from .models import Situacao, AssuntoSolicitacao, Solicitacao

class SolicitacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        depth=1
        fields = ['id', 'assuntosolicitacao', 'endereco', 'numero', 'complemento', 'bairro', 'latitude', 'longitude', 'descricao', 'situacao', 'dt_inclusao']
