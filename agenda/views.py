from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from agenda.models import Assunto, Agenda
from agenda.serializers import AssuntoSerializer, AgendaSerializer

# Create your views here.

class AssuntosList(APIView):
    def get(self, request, format=None):
        assuntos = Assunto.objects.all()
        serializer = AssuntoSerializer(assuntos, many=True)
        return Response(serializer.data)

class AgendasList(APIView):
    def get(self, request, format=None):
        agendas = Agenda.objects.all()

        serializer_context = {
            'request': request
        }

        serializer = AgendaSerializer(agendas, many=True, context=serializer_context)
        return Response(serializer.data)
