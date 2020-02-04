from .models import Historico_Alerta, Responsavel, Alerta
from django.contrib.auth.models import User, Group

from rest_framework import serializers


class ResponsavelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responsavel
        fields = ['nome', 'celular', 'user', 'dt_inclusao']

#class SituacaoSerializer(serializers.HyperlinkedModelSerializer):
class SituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        url = serializers.HyperlinkedIdentityField(
#            many=True,
#            read_only=True,
            view_name="dcivil:alerta-detail",
        )
        model = Historico_Alerta
        fields = ['alerta', 'dt_inclusao']
#        fields = '__all__'
