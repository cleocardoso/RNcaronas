from django.db import models
from usuario.models import usuario
from Carona.models import Carona

class pedirCarona(models.Model):
    dataPedCarona = models.DateField(null=True, blank=True)
    quantidadeVagas = models.IntegerField('quantidade de vagas')
    total = models.DecimalField('total', max_digits=7, decimal_places=2, blank=True, null=True)
    carona = models.ForeignKey(Carona, models.CASCADE, name='carona', related_name='Carona')
    Usuario = models.ForeignKey(usuario, models.CASCADE, name='usuario', related_name='Usuario')
    statusConcluido= models.BooleanField(null=True, blank=True, default=False)
    statusAndamento = models.BooleanField(null=True, blank=True, default=False)
    statusCancelado = models.BooleanField(null=True, blank=True, default=False)


    class Meta:
        db_table = 'pedir_carona'
