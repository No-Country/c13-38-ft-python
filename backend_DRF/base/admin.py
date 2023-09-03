from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,
    Espacio,
    ParticipantesEspacio,
    Tablero,
    ParticipantesTablero,
    Lista,
    Tarjeta,
    Comentario,
    Respuesta,
)

# Register your models here.

lista_modelos = [
    Tablero,
    Espacio,
    ParticipantesEspacio,
    ParticipantesTablero,
    Lista,
    Tarjeta,
    Comentario,
    Respuesta
]

admin.site.register(User, UserAdmin)
admin.site.register(lista_modelos)
