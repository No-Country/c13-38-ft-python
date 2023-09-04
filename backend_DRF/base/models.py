from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=30)
    objects = UserManager()


class Espacio(models.Model):
    nombre_espacio = models.CharField(max_length=30, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)
    participantes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="ParticipantesEspacio", related_name="participantes_espacio")
    creador_espacio = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_espacio


class ParticipantesEspacio(models.Model):
    id_participante = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    id_espacio = models.ForeignKey(
        Espacio, null=False, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_participante', 'id_espacio'], name='unique_participants_espacio')
        ]
    
    def __str__(self):
        return f'Usuario: {self.id_participante.username} --- Espacio: {self.id_espacio.nombre_espacio}'


class Tablero(models.Model):
    nombre_tablero = models.CharField(max_length=30, null=False)
    creador_tablero = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    espacio_id = models.ForeignKey(Espacio, null=False, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.nombre_tablero


class Lista(models.Model):
    creador_lista = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    tablero_relacionado = models.ForeignKey(
        Tablero, null=True, on_delete=models.CASCADE)
    nombre_lista = models.CharField(max_length=30, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre_lista


class Tarjeta(models.Model):
    creador_tarjeta = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    lista_relacionada = models.ForeignKey(
        Lista, null=True, on_delete=models.CASCADE)
    titulo_tarjeta = models.CharField(max_length=30, null=True)
    descripcion_tarjeta = models.CharField(max_length=256, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.titulo_tarjeta


class Comentario(models.Model):
    tarjeta_relacionada = models.ForeignKey(
        Tarjeta, null=True, on_delete=models.CASCADE)
    creador_comentario = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    texto_comentario = models.CharField(max_length=256, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.texto_comentario[0:100]


class Respuesta(models.Model):
    comentario_relacionado = models.ForeignKey(
        Comentario, null=True, on_delete=models.CASCADE)
    creador_respuesta = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    texto_respuesta = models.CharField(max_length=256, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.texto_respuesta[0:100]
