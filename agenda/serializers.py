from rest_framework import serializers

from .models import Assunto, Agenda

class AssuntoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assunto
        fields = ['id', 'descricao']

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        depth=1
        fields = ['id', 'titulo', 'descricao', 'assunto', 'dt_evento']
