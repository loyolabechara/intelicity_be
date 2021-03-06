from .models import Usuario, Estado, Cidade, Bairro
from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
    #        fields = '__all__'
        fields = ('id', 'cpf', 'dt_nascimento', 'sexo', 'celular', 'endereco', 'numero', 'complemento')


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
#        fields = '__all__'
        fields = ('id', 'nome')


class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
#        fields = '__all__'
        fields = ('id', 'nome')


class BairroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bairro
#        fields = '__all__'
        fields = ('id', 'nome')
