from django.db import models
from usuario.models import usuario
from Carona.models import Carona

class pedirCarona(models.Model):
    dataPedCarona = models.DateField(null=True, blank=True, name='data_carona')
    quantidadeVagas = models.IntegerField('quantidade de vagas', name='quantidade_vagas')
    total = models.DecimalField('total', max_digits=7, decimal_places=2, blank=True, null=True)
    carona = models.ForeignKey(Carona, models.CASCADE, name='carona', related_name='Carona')
    Usuario = models.ForeignKey(usuario, models.CASCADE, name='usuario', related_name='Usuario')
    statusConcluido= models.BooleanField(null=True, name='status_concluido', blank=True, default=False)
    statusAndamento = models.BooleanField(null=True, name='status_andamento', blank=True, default=False)
    statusCancelado = models.BooleanField(null=True, name='status_cancelado', blank=True, default=False)


    class Meta:
        db_table = 'pedir_carona'
