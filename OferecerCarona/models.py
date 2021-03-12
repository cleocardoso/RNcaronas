from django.db import models
from usuario.models import usuario

class oferecerCarona(models.Model):
    dataOfCarona = models.DateField(null=True, blank=True)
    quantidadeVagas = models.IntegerField('quantidade de vagas', blank=True, null=True)
    valorCarona = models.DecimalField('valor', max_digits=7, decimal_places=2, blank=True, null=True)
    Usuario = models.ForeignKey(usuario, models.CASCADE, related_name='usuario')


    class Meta:
        db_table = 'oferecerCarona'