from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tablero, Espacio
from base.api.serializers import ParticipantesEspacioSerializer


@receiver(post_save, sender=Espacio)
def agregar_creador_como_participante_espacio(sender, created, instance, **kwargs):
    if created:
        nuevo_participante = ParticipantesEspacioSerializer(data={
            'id_participante': instance.creador_espacio.id,
            'id_espacio': instance.id
        })
        if nuevo_participante.is_valid():
            nuevo_participante.save()
