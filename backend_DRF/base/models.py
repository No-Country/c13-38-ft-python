from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=20)
    objects = UserManager()


class Tablero(models.Model):
    nombre_tablero = models.CharField(max_length=50, null=False)
    creador_tablero = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    participantes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="ParticipantesTablero", related_name="participantes")
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):  # Para que 'nombre' represente el objeto en la admin page
        return self.nombre_tablero


class ParticipantesTablero(models.Model):
    id_participante = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    id_tablero = models.ForeignKey(
        Tablero, null=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_participante', 'id_tablero'], name='unique_participants')
        ]

    def __str__(self):  # Para que 'nombre' represente el objeto en la admin page
        return f'Usuario: {self.id_participante.username} --- Tablero: {self.id_tablero.nombre_tablero}'


class Lista(models.Model):
    creador_lista = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    tablero_relacionado = models.ForeignKey(
        Tablero, null=True, on_delete=models.CASCADE)
    nombre_lista = models.CharField(max_length=50, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):  # Para que 'nombre' represente el objeto en la admin page
        return self.nombre_lista


class Tarjeta(models.Model):
    creador_tarjeta = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    lista_relacionada = models.ForeignKey(
        Lista, null=True, on_delete=models.CASCADE)
    titulo_tarjeta = models.CharField(max_length=50, null=True)
    descripcion_tarjeta = models.CharField(max_length=256, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):  # Para que 'nombre' represente el objeto en la admin page
        return self.titulo_tarjeta


class Comentario(models.Model):
    tarjeta_relacionada = models.ForeignKey(
        Tarjeta, null=True, on_delete=models.CASCADE)
    creador_comentario = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    texto_comentario = models.CharField(max_length=256, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):  # Para que 'nombre' represente el objeto en la admin page
        return self.texto_comentario[0:100]


class Respuesta(models.Model):
    comentario_relacionado = models.ForeignKey(
        Comentario, null=True, on_delete=models.CASCADE)
    creador_respuesta = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    texto_respuesta = models.CharField(max_length=256, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):  # Para que 'nombre' represente el objeto en la admin page
        return self.texto_respuesta[0:100]
