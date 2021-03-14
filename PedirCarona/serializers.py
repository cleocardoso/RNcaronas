from rest_framework import serializers
from PedirCarona.models import pedirCarona



class PedCaronaSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedirCarona
        #fields = ('id', 'dataPedCarona','quantidadeVagas','total','statusConcluido','statusAndamento','statusCancelado')
        fields = ('__all__')