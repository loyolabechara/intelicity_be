from django.shortcuts import render
from accounts.serializers import UserSerializer, GroupSerializer, UsuarioSerializer, EstadoSerializer, CidadeSerializer, BairroSerializer
from rest_framework import viewsets
from accounts.models import Usuario, Estado, Cidade, Bairro
from django.contrib.auth.models import User, Group

from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

# Create your views here.


# /////////////////////////////////

class UsuarioList(APIView):
    """
    List all usuarios, or create a new usuario.
    """
    def get(self, request, format=None):
        usuarios = Usuario.objects.all()
        serializer_context = {
            'request': request
        }

        serializer = UsuarioSerializer(usuarios, many=True, context=serializer_context)
#        serializer = CidadeSerializer(cidades, context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
 
        if serializer.is_valid():
            print ('dentro do valid')
            print('cpf:', request.POST.get('cpf'))

            user = User.objects.create_user(request.POST.get('cpf'), request.POST.get('email'), 'fk#gjdfp%je*j43')

            # Update fields and then save again
            user.first_name = request.POST.get('nome')
            user.last_name = ''
            user.save()

            token = Token.objects.create(user=user)
            print(token.key)

            bairro = Bairro.objects.get(id=request.POST.get('bairro_id'))

            cpf = request.POST.get('cpf')

            usuario = Usuario(user=user, cpf=cpf,
                celular=request.POST.get('celular'),
                sexo=request.POST.get('sexo'),
                endereco=request.POST.get('endereco'),
                numero=request.POST.get('numero'),
                complemento=request.POST.get('complemento'),
                bairro=bairro,
                cep=request.POST.get('cep'),
                dt_nascimento=request.POST.get('dt_nascimento')
            )
            usuario.save()

#            print('id:', user.id)
#            print('data:', serializer.data)

            content = {'id': user.id, 'token': token.key}
            return Response(content, status=status.HTTP_201_CREATED)

#            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
