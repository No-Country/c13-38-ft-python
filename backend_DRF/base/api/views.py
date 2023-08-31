from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import (
    RegistrationSerializer,
    TableroSerializer,
    ListaSerializer,
    TarjetaSerializer,
    ComentarioSerializer,
    RespuestaSerializer,
)
from base.models import (
    User,
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
def tablero(request):
    user = request.user
    if request.method == 'GET':
        tableros = user.tablero_set.all()
        serializer = TableroSerializer(tableros, many=True)
        return Response(serializer.data)
    else:
        serializer = TableroSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, 201)
