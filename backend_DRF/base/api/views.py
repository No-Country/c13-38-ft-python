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
    EspacioSerializer,
    ParticipantesEspacioSerializer,
    TableroSerializer,
    ListaSerializer,
    TarjetaSerializer,
    ComentarioSerializer,
    RespuestaSerializer,
)
from base.models import (
    User,
    Espacio,
    ParticipantesEspacio,
    Tablero,
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
def espacio(request):
    user = request.user
    if request.method == 'GET':
        espacios = [espacio.id_espacio for espacio in user.participantesespacio_set.all()]
        serializer = EspacioSerializer(espacios, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        request.data['creador_espacio'] = user.id
        serializer = EspacioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_espacio(request, pk):
    user = request.user
    try:
        participacion = ParticipantesEspacio.objects.get(id_participante=user.id, id_espacio=pk)
        espacio = participacion.id_espacio
    except ParticipantesEspacio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tableros_espacio = Tablero.objects.filter(espacio_id=espacio)
        serializer_tablero = TableroSerializer(tableros_espacio, many=True)
        serializer_espacio = EspacioSerializer(espacio)
        info_espacio = serializer_espacio.data
        info_espacio.update({'tableros': serializer_tablero.data})
        return Response(info_espacio)

    if user != espacio.creador_espacio:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        request.data['creador_espacio'] = espacio.creador_espacio.id
        serializer = EspacioSerializer(instance=espacio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        espacio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def participaciones_espacios(request, pk):
    user = request.user
    participantes_agregados = None
    participantes_eliminados = None
    try:
        espacio = user.espacio_set.get(id=pk)
    except Espacio.DoesNotExist:
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

            serializer = ParticipantesEspacioSerializer(data={
                'id_participante': participante.id,
                'id_espacio': espacio.id
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
                eliminar = ParticipantesEspacio.objects.get(
                    id_participante=participante.id,
                    id_espacio=espacio.id
                )
            except ParticipantesEspacio.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            eliminar.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tablero(request):
    user = request.user
    if request.method == 'GET':
        tableros = user.tablero_set.all()
        serializer = TableroSerializer(tableros, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        request.data['creador_tablero'] = user.id
        if request.data.get('espacio_id', None):
            try:
                espacio = Espacio.objects.get(id=request.data['espacio_id'])
            except Espacio.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if espacio not in user.espacio_set.all():
                return Response(status=status.HTTP_403_FORBIDDEN)
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
        tablero = Tablero.objects.get(id=pk)
    except Tablero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tablero_pertenece_a_user = tablero.creador_tablero.id == user.id
    user_en_espacio = tablero.espacio_id in [
        participacion.id_espacio for participacion in user.participantesespacio_set.all()
    ]

    if tablero_pertenece_a_user == False and user_en_espacio == False:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer_tablero = TableroSerializer(tablero)
        serializer_listas = ListaSerializer(tablero.lista_set.all(), many=True)
        info_tablero = serializer_tablero.data
        info_listas = serializer_listas.data

        for lista in info_listas:
            tarjetas = TarjetaSerializer(Tarjeta.objects.filter(
                lista_relacionada=lista['id']), many=True)
            lista.update({'tarjetas': tarjetas.data})

        info_tablero.update({'listas': info_listas})
        return Response(info_tablero)

    if tablero_pertenece_a_user == False:
            return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        request.data['creador_tablero'] = tablero.creador_tablero.id
        request.data['espacio_id'] = tablero.espacio_id.id
        serializer = TableroSerializer(instance=tablero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        tablero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lista(request):
    user = request.user
    request.data['creador_lista'] = user.id
    serializer = ListaSerializer(data=request.data)
    if serializer.is_valid():
        tablero = Tablero.objects.get(id=request.data['tablero_relacionado'])
        try:
            ParticipantesEspacio.objects.get(
                id_participante=user.id, id_espacio=tablero.espacio_id)
        except ParticipantesEspacio.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_lista(request, pk):
    user = request.user
    try:
        lista = Lista.objects.get(id=pk)
    except Lista.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if user != lista.creador_lista:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        request.data['creador_lista'] = lista.creador_lista.id
        request.data['tablero_relacionado'] = lista.tablero_relacionado.id
        serializer = ListaSerializer(instance=lista, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        lista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tarjeta(request):
    user = request.user
    request.data['creador_tarjeta'] = user.id
    serializer = TarjetaSerializer(data=request.data)
    if serializer.is_valid():
        lista_relacionada = Lista.objects.get(id=request.data['lista_relacionada'])
        tablero_relacionado = lista_relacionada.tablero_relacionado
        try:
            ParticipantesEspacio.objects.get(
                id_participante=user.id, id_espacio=tablero_relacionado.espacio_id)
        except ParticipantesEspacio.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_tarjeta(request, pk):
    user = request.user
    try:
        tarjeta = Tarjeta.objects.get(id=pk)
    except Tarjeta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    lista_relacionada = Lista.objects.get(id=tarjeta.lista_relacionada.id)
    tablero_relacionado = lista_relacionada.tablero_relacionado
 
    try:
        ParticipantesEspacio.objects.get(
            id_participante=user.id, id_espacio=tablero_relacionado.espacio_id)
    except ParticipantesEspacio.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer_tarjeta = TarjetaSerializer(tarjeta)
        serializer_comentarios = ComentarioSerializer(tarjeta.comentario_set.all(), many=True)
        info_tarjeta = serializer_tarjeta.data
        info_comentarios = serializer_comentarios.data

        for comentario in info_comentarios:
            respuestas = RespuestaSerializer(Respuesta.objects.filter(
                comentario_relacionado=comentario['id']), many=True)
            comentario.update({'respuestas': respuestas.data})

        info_tarjeta.update({'comentarios': info_comentarios})
        return Response(info_tarjeta)

    if user != tarjeta.creador_tarjeta:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        request.data['creador_tarjeta'] = tarjeta.creador_tarjeta.id
        serializer = TarjetaSerializer(instance=tarjeta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        tarjeta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comentario(request):
    user = request.user
    request.data['creador_comentario'] = user.id
    serializer = ComentarioSerializer(data=request.data)
    if serializer.is_valid():
        tarjeta_relacionada = Tarjeta.objects.get(id=request.data['tarjeta_relacionada'])
        lista_relacionada = tarjeta_relacionada.lista_relacionada
        tablero_relacionado = lista_relacionada.tablero_relacionado
        try:
            ParticipantesEspacio.objects.get(
                id_participante=user.id, id_espacio=tablero_relacionado.espacio_id)
        except ParticipantesEspacio.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def respuesta(request):
    user = request.user
    request.data['creador_respuesta'] = user.id
    serializer = RespuestaSerializer(data=request.data)
    if serializer.is_valid():
        comentario_relacionado = Comentario.objects.get(id=request.data['comentario_relacionado'])
        tarjeta_relacionada = comentario_relacionado.tarjeta_relacionada
        lista_relacionada = tarjeta_relacionada.lista_relacionada
        tablero_relacionado = lista_relacionada.tablero_relacionado
        try:
            ParticipantesEspacio.objects.get(
                id_participante=user.id, id_espacio=tablero_relacionado.espacio_id)
        except ParticipantesEspacio.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
