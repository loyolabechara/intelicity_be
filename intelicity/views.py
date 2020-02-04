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
 
        print ('antes do valid')

        if serializer.is_valid():
            print ('dentro do valid')
            print('id:', request.POST.get('user_id'))
            print('cpf:', request.POST.get('cpf'))
            usuario = User.objects.get(id=request.POST.get('user_id'))
            bairro = Bairro.objects.get(id=request.POST.get('bairro_id'))

            tmp = serializer.save(user=usuario, bairro=bairro)
#                        temp_ocorrencia = form.save(commit=False)
#            tmp.user = 1
            tmp.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# /////////////////////////////////

class EstadoList(APIView):
    """
    List all estados, or create a new estado.
    """
    def get(self, request, format=None):
        estados = Estado.objects.all()
        serializer_context = {
            'request': request
        }

        serializer = EstadoSerializer(estados, many=True, context=serializer_context)
#        serializer = EstadoSerializer(estados, context=serializer_context)
        return Response(serializer.data)


# /////////////////////////////////

class CidadeList(APIView):
    """
    List all cidades, or create a new cidade.
    """
    def get(self, request, id, format=None):
        cidades = Cidade.objects.filter(estado=id)
        serializer_context = {
            'request': request
        }

        serializer = CidadeSerializer(cidades, many=True, context=serializer_context)
#        serializer = CidadeSerializer(cidades, context=serializer_context)
        return Response(serializer.data)


# /////////////////////////////////

class BairroList(APIView):
    """
    List all bairros, or create a new bairro.
    """
    def get(self, request, id, format=None):
        bairros = Bairro.objects.filter(cidade=id)
        serializer_context = {
            'request': request
        }

        serializer = BairroSerializer(bairros, many=True, context=serializer_context)
#        serializer = CidadeSerializer(cidades, context=serializer_context)
        return Response(serializer.data)
