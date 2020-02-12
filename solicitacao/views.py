from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from solicitacao.models import AssuntoSolicitacao, Situacao, Solicitacao, User
from solicitacao.serializers import SolicitacoesSerializer

# Create your views here.

class SolicitacoesList(APIView):
    def get(self, request, format=None):
        usuario = User.objects.get(username=request.user.username)
        solicitacoes = Solicitacao.objects.filter(user=usuario)
        serializer = SolicitacoesSerializer(solicitacoes, many=True)
        return Response(serializer.data)
