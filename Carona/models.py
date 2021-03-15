from OferecerCarona.models import oferecerCarona
from django.db import models

# Create your models here.
class Carona(models.Model):
    destino = models.CharField(max_length=255, blank=True, null=True)
    partida = models.CharField(max_length=255, blank=True, null=True)
    oferecerCarona = models.ForeignKey(oferecerCarona, name='oferecer_carona', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'carona'
