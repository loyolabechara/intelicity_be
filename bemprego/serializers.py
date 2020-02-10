from rest_framework import serializers

from .models import Escolaridade, Vaga, Cargo

class EscolaridadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escolaridade
        fields = ['id', 'descricao']

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        depth=1
        fields = ['id', 'cargo', 'sexo', 'experiencia', 'escolaridade', 'dt_fim', 'dt_inclusao']
