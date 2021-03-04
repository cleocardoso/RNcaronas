from rest_framework import serializers
from .models import usuario, oferecerCarona, pedirCarona


class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('id', 'nome', 'email', 'senha', 'nome', 'foto', 'active')

class oferecerCaronaSerializer(serializers.ModelSerializer):
    class Meta:
        model = oferecerCarona
        fields = ('id', 'dataOfCarona', 'destino', 'partida', 'quantidadeVagas', 'valorCarona')

class pedirCaronaSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedirCarona
        fields = ('id', 'dataPedCarona', 'destino', 'partida', 'quantidadeVagas')
