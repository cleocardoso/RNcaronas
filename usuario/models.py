from django.db import models
from django.contrib.auth.models import User


class usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="user", blank=True, null=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #oferecerCarona = models.OneToOneField("oferecerCarona", on_delete=models.CASCADE, related_name="usuario")
    #pedirCarona = models.ForeignKey("pedirCarona", on_delete=models.CASCADE, related_name="usuario")

    def __str__(self):

        return str(self.id)

    class Meta:
        db_table = 'usuario'

class oferecerCarona(models.Model):
    dataOfCarona = models.DateField(null=True, blank=True)
    destino = models.CharField(max_length=255, blank=True, null=True)
    partida = models.CharField(max_length=255, blank=True, null=True)
    quantidadeVagas = models.IntegerField('quantidade de vagas', blank=True, null=True)
    valorCarona = models.DecimalField('valor', max_digits=7, decimal_places=2, blank=True, null=True)
    #usuario = models.OneToManyField(usuario, on_delete=models.SET_NULL, null=True)
    #usuario = models.OneToManyField('usuario')
    usuario = models.ForeignKey(usuario, models.CASCADE, related_name='oferecerCarona')


    class Meta:
        db_table = 'oferecerCarona'

class pedirCarona(models.Model):
    dataPedCarona = models.DateField(null=True, blank=True)
    quantidadeVagas = models.IntegerField('quantidade de vagas')
    destino = models.CharField(max_length=255)
    buscarCarona = models.CharField(max_length=255)
    partida = models.CharField(max_length=255)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE,related_name="pedirCarona")
    class Meta:
        db_table = 'pedirCarona'

