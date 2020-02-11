from rest_framework import serializers

from .models import Categoria_Telefone, Telefone

class CategoriaTelefoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria_Telefone
        fields = ['id', 'descricao']

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        depth=1
        fields = ['id', 'categoria_telefone', 'nome', 'numero', 'mensageiro']
