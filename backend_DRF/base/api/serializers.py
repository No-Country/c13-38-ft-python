from rest_framework import serializers
from base.models import (
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


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = '__all__'
    

class ParticipantesEspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantesEspacio
        fields = '__all__'


class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = '__all__'


class ParticipantesTableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantesTablero
        fields = '__all__'


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'
