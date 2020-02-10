from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from bemprego.models import Escolaridade, Vaga, Cargo
from bemprego.serializers import EscolaridadeSerializer, VagaSerializer

# Create your views here.

class EscolaridadesList(APIView):
    def get(self, request, format=None):
        escolaridades = Escolaridade.objects.all()
        serializer = EscolaridadeSerializer(escolaridades, many=True)
        return Response(serializer.data)

class VagasList(APIView):
    def get(self, request, escolaridade, format=None):
        vagas = Vaga.objects.filter(escolaridade=escolaridade)

        serializer_context = {
            'request': request
        }

        serializer = VagaSerializer(vagas, many=True, context=serializer_context)
        return Response(serializer.data)
