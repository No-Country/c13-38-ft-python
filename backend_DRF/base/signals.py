from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tablero, ParticipantesTablero
from base.api.serializers import ParticipantesTableroSerializer


@receiver(post_save, sender=Tablero)
def agregar_creador_como_participante(sender, created, instance, **kwargs):
    if created:
        nuevo_participante = ParticipantesTableroSerializer(data={
            'id_participante': instance.creador_tablero.id,
            'id_tablero': instance.id
        })
        if nuevo_participante.is_valid():
            nuevo_participante.save()
