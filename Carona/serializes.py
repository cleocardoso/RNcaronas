from rest_framework import serializers

from Carona.models import Carona


class CaronaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carona
        fields = ('id', 'destino', 'partida')