from PedirCarona.models import pedirCarona
from usuario import serializers


class PedCaronaSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedirCarona
        fields = ('id', 'dataPedCarona','quantidadeVagas')