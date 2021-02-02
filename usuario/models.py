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