from rest_framework import serializers
from .models import usuario


class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('id', 'nome', 'email', 'senha', 'nome', 'foto', 'active')




