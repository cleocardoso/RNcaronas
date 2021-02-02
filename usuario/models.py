from django.db import models
from django.contrib.auth.models import User


class usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    foto = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'usuario'

class oferecerCarona(models.Model):
    dataOf = models.DateTimeField()
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'oferecerCarona'

class pedirCarona(models.Model):
    dataPd = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pedirCarona'


class rota(models.Model):
    destino = models.CharField(max_length=255)
    partida = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'rota'