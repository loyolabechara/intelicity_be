from rest_framework import serializers

from .models import Assunto, Evento

class AssuntoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assunto
        fields = ['id', 'descricao']

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        depth=1
        fields = ['id', 'titulo', 'descricao', 'assunto', 'dt_evento']
