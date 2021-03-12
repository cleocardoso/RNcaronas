from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Carona.models import Carona
from Carona.serializes import CaronaSerializer


class CaronaViewSet(viewsets.ModelViewSet):
    queryset = Carona.objects.all()
    serializer_class = CaronaSerializer
