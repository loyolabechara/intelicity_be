from dcivil.serializers import ResponsavelSerializer, SituacaoSerializer, PontoApoioSerializer

from dcivil.models import Responsavel, Historico_Alerta, Ponto_Apoio

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class ResponsavelList(APIView):
    def get(self, request, format=None):
        responsavel = Responsavel.objects.all()
        serializer = ResponsavelSerializer(responsavel, many=True)
        return Response(serializer.data)

from rest_framework.generics import(
    ListCreateAPIView
)

class SituacaoList(APIView):
    def get(self, request, format=None):
        historico = Historico_Alerta.objects.all().order_by('-dt_inclusao')[0]
        serializer_context = {
            'request': request
        }

        serializer = SituacaoSerializer(historico, many=False, context=serializer_context)
        return Response(serializer.data)

class SituacoesList(APIView):
    def get(self, request, format=None):
        historico = Historico_Alerta.objects.all().order_by('-dt_inclusao')
        serializer_context = {
            'request': request
        }

        serializer = SituacaoSerializer(historico, many=True, context=serializer_context)
        return Response(serializer.data)

class PontosApoioList(APIView):
    def get(self, request, format=None):
        pontos = Ponto_Apoio.objects.all().order_by('nome')
        serializer_context = {
            'request': request
        }

        serializer = PontoApoioSerializer(pontos, many=True, context=serializer_context)
        return Response(serializer.data)
