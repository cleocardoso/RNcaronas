from django.db import models
from usuario.models import usuario
from Carona.models import Carona

class pedirCarona(models.Model):
    dataPedCarona = models.DateField(null=True, blank=True)
    quantidadeVagas = models.IntegerField('quantidade de vagas')
    carona = models.ForeignKey(Carona, models.CASCADE, related_name='Carona')
    Usuario = models.ForeignKey(usuario, models.CASCADE, related_name='Usuario')
    status = models.BooleanField(null=True, blank=True, default=False)
    class Meta:
        db_table = 'pedirCarona'
