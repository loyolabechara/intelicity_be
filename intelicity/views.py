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


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

# =======================

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

# ===========

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# /////////////////////////////////

class EstadoList(APIView):
    """
    Lista todos os estados
    """
    def get(self, request, format=None):
        estados = Estado.objects.all()
        serializer_context = {
            'request': request
        }

        serializer = EstadoSerializer(estados, many=True, context=serializer_context)
        return Response(serializer.data)


# /////////////////////////////////

class CidadeList(APIView):
    """
    Lista todas as cidades de um estado
    """
    def get(self, request, id, format=None):
        cidades = Cidade.objects.filter(estado=id)
        serializer_context = {
            'request': request
        }

        serializer = CidadeSerializer(cidades, many=True, context=serializer_context)
        return Response(serializer.data)


# /////////////////////////////////

class BairroList(APIView):
    """
    Lista todos os bairros de uma cidade
    """
    def get(self, request, id, format=None):
        bairros = Bairro.objects.filter(cidade=id)
        serializer_context = {
            'request': request
        }

        serializer = BairroSerializer(bairros, many=True, context=serializer_context)
        return Response(serializer.data)
