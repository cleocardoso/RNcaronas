from django.db import models
from django.contrib.auth.models import User


class usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="media/%y/%m",blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.id)

    class Meta:
        db_table = 'usuario'

class oferecerCarona(models.Model):

    dataOferecer = models.DateTimeField(auto_now=True)
    destino = models.CharField(max_length=255)
    partida = models.CharField(max_length=255)
    quantidadeVagas = models.IntegerField('quantidade de vagas')
    valorCarona = models.DecimalField('valor', max_digits=7, decimal_places=2)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'oferecerCarona'

class pedirCarona(models.Model):
    dataPedir = models.DateTimeField(auto_now=True)
    quantidadeVagas = models.IntegerField('quantidade de vagas')
    destino = models.CharField(max_length=255)
    buscarCarona = models.CharField(max_length=255)
    partida = models.CharField(max_length=255)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    class Meta:
        db_table = 'pedirCarona'

