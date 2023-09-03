from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.db import IntegrityError
from .serializers import (
    RegistrationSerializer,
    TableroSerializer,
    ParticipantesTableroSerializer,
    ListaSerializer,
    TarjetaSerializer,
    ComentarioSerializer,
    RespuestaSerializer,
)
from base.models import (
    User,
    Espacio,
    Tablero,
    ParticipantesTablero,
    Lista,
    Tarjeta,
    Comentario,
    Respuesta,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tablero(request):
    user = request.user
    if request.method == 'GET':
        tableros = [tablero.id_tablero for tablero in user.participantestablero_set.all()]
        serializer = TableroSerializer(tableros, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        request.data['creador_tablero'] = user.id
        serializer = TableroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_tablero(request, pk):
    user = request.user
    try:
        participacion = ParticipantesTablero.objects.get(id_participante=user.id, id_tablero=pk)
        tablero = participacion.id_tablero
    except ParticipantesTablero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TableroSerializer(tablero)
        return Response(serializer.data)

    if request.method == 'PUT':
        request.data['creador_tablero'] = tablero.creador_tablero.id
        serializer = TableroSerializer(instance=tablero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        tablero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def participaciones_tableros(request, pk):
    user = request.user
    participantes_agregados = None
    participantes_eliminados = None
    try:
        tablero = user.tablero_set.get(id=pk)
    except Tablero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        try:
            participantes_agregados = request.data['participantes_agregados']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(participantes_agregados, list) or len(participantes_agregados) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        for username in participantes_agregados:
            try:
                participante = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = ParticipantesTableroSerializer(data={
                'id_participante': participante.id,
                'id_tablero': tablero.id
            })
            if serializer.is_valid():
                try:
                    serializer.save()
                except IntegrityError:
                   return Response(status=status.HTTP_409_CONFLICT)
                return Response(status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            participantes_eliminados = request.data['participantes_eliminados']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(participantes_eliminados, list) or len(participantes_eliminados) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if User.objects.get(username=user).username in participantes_eliminados:
            return Response(status=status.HTTP_403_FORBIDDEN)

        for username in participantes_eliminados:
            try:
                participante = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            try:
                eliminar = ParticipantesTablero.objects.get(
                    id_participante=participante.id,
                    id_tablero=tablero.id
                )
            except ParticipantesTablero.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            eliminar.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
