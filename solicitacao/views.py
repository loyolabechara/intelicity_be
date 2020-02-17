from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from solicitacao.models import AssuntoSolicitacao, Situacao, Solicitacao, User
from solicitacao.serializers import AssuntosSerializer, SolicitacoesSerializer, SolicitacaoSerializer

from accounts.models import Bairro

from rest_framework import status

# Create your views here.

class Solicitacoes(APIView):
    def get(self, request, format=None):
        usuario = User.objects.get(username=request.user.username)
        solicitacoes = Solicitacao.objects.filter(user=usuario)
        serializer = SolicitacoesSerializer(solicitacoes, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = SolicitacaoSerializer(data=request.data)
 
        print ('antes do valid')

        if serializer.is_valid():
            print ('dentro do valid')
            print('id:', request.POST.get('user_id'))
            print('cpf:', request.POST.get('cpf'))

            assunto = AssuntoSolicitacao.objects.get(id=request.POST.get('assuntosolicitacao_id'))
            usuario = User.objects.get(username=request.user.username)
            bairro = Bairro.objects.get(id=request.POST.get('bairro_id'))

            tmp = serializer.save(user=usuario, bairro=bairro, assuntosolicitacao=assunto)
#                        temp_ocorrencia = form.save(commit=False)
#            tmp.user = 1
            tmp.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssuntosList(APIView):
    def get(self, request, format=None):
        assuntos = AssuntoSolicitacao.objects.all()
        serializer = AssuntosSerializer(assuntos, many=True)
        return Response(serializer.data)
