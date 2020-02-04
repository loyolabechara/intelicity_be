from dcivil.serializers import ResponsavelSerializer, SituacaoSerializer

from dcivil.models import Responsavel, Historico_Alerta

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
        print('inicio')
        historico = Historico_Alerta.objects.all()
        serializer_context = {
            'request': request
        }

        print(historico)
        serializer = SituacaoSerializer(historico, many=True, context=serializer_context)
        return Response(serializer.data)
