from rest_framework import serializers
from .models import Evento, Subtarea


class SubtareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtarea
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    subtareas = SubtareaSerializer(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = '__all__'