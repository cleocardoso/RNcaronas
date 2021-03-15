from django.db import models
from usuario.models import usuario

class oferecerCarona(models.Model):
    dataOfCarona = models.DateField(null=True, name='data_carona', blank=True)
    quantidadeVagas = models.IntegerField('quantidade de vagas', name='quantidade_vagas', blank=True, null=True)
    valorCarona = models.DecimalField('valor', max_digits=7, name='valor_carona', decimal_places=2, blank=True, null=True)
    ValorTotal = models.DecimalField('valor', max_digits=7, name='valor_total', decimal_places=2, blank=True, null=True)
    Usuario = models.ForeignKey(usuario, models.CASCADE, name='usuario', related_name='usuario')


    class Meta:
        db_table = 'oferecer_carona'
