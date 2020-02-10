from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from agenda.models import Assunto, Evento
from agenda.serializers import AssuntoSerializer, EventoSerializer

# Create your views here.

class AssuntosList(APIView):
    def get(self, request, format=None):
        assuntos = Assunto.objects.all()
        serializer = AssuntoSerializer(assuntos, many=True)
        return Response(serializer.data)

class EventosList(APIView):
    def get(self, request, assunto, format=None):
        eventos = Evento.objects.filter(assunto=assunto)

        serializer_context = {
            'request': request
        }

        serializer = EventoSerializer(eventos, many=True, context=serializer_context)
        return Response(serializer.data)
