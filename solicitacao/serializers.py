from rest_framework import serializers

from .models import Situacao, AssuntoSolicitacao, Solicitacao


class AssuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssuntoSolicitacao
        fields = ['id', 'descricao']

class SolicitacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        depth=1
        fields = ['id', 'assuntosolicitacao', 'endereco', 'numero', 'complemento', 'bairro', 'latitude', 'longitude', 'descricao', 'situacao', 'dt_inclusao']

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = ['assuntosolicitacao_id', 'descricao', 'endereco', 'numero', 'complemento', 'bairro_id', 'latitude', 'longitude']
