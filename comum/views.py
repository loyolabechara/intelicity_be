from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from comum.models import Categoria_Telefone, Telefone
from comum.serializers import CategoriaTelefoneSerializer, TelefoneSerializer

# Create your views here.

class CategoriaTelefoneList(APIView):
    def get(self, request, format=None):
        categorias = Categoria_Telefone.objects.all()
        serializer = CategoriaTelefoneSerializer(categorias, many=True)
        return Response(serializer.data)

class TelefoneList(APIView):
    def get(self, request, item, format=None):
        telefones = Telefone.objects.filter(categoria_telefone=item)

        serializer_context = {
            'request': request
        }

        serializer = TelefoneSerializer(telefones, many=True, context=serializer_context)
        return Response(serializer.data)
