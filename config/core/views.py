from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Evento, Subtarea
from .serializers import EventoSerializer


@api_view(['GET'])
def health_check(request):
    return Response({
        "status": "ok",
        "message": "API del Organizador de Eventos funcionando correctamente"
    })


@api_view(['GET', 'POST'])
def eventos(request):
    if request.method == 'GET':
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EventoSerializer(data=request.data)

        if serializer.is_valid():
            evento = serializer.save()

            Subtarea.objects.create(
                evento=evento,
                nombre='Reservar salón',
                plazo=evento.plazo_limite,
                horas_estimadas=2
            )

            Subtarea.objects.create(
                evento=evento,
                nombre='Enviar invitaciones',
                plazo=evento.plazo_limite,
                horas_estimadas=2
            )

            Subtarea.objects.create(
                evento=evento,
                nombre='Confirmar catering',
                plazo=evento.plazo_limite,
                horas_estimadas=2
            )

            return Response(
                EventoSerializer(evento).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )