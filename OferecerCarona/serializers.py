from rest_framework import serializers
from OferecerCarona.models import oferecerCarona

class oferecerCaronaSerializer(serializers.ModelSerializer):
    class Meta:
        model = oferecerCarona
        fields = ('id', 'dataOfCarona', 'quantidadeVagas', 'valorCarona','ValorTotal')