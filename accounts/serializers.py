from .models import Usuario, Cidade, Bairro
from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UsuarioSerializer(serializers.ModelSerializer):

#    serializers.chave = '123'
#    serializers.cinema = 'http://127.0.0.1:8000/cinema/1/'
#    chave = '123'
#    serializers.CharField(source='chave') = '123'

    class Meta:
        model = Usuario
    #        fields = '__all__'
        fields = ('id', 'cpf', 'email', 'dt_nascimento', 'sexo', 'celular', 'endereco', 'numero', 'complemento')


class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
#        fields = '__all__'
        fields = ('id', 'nome')


class BairroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bairro
#        fields = '__all__'
        fields = ('id', 'cidade_id', 'nome')
