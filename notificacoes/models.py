from django.db import models

# Create your models
from usuario.models import usuario
from PedirCarona.models import pedirCarona

class notificacao(models.Model):
    data = models.DateField(null=True, blank=True)
    mensagem = models.CharField(max_length=255)
    PedidoSolicidato = models.ForeignKey(pedirCarona, models.CASCADE, related_name='pedirCarona')
    UsuarioEnvia = models.ForeignKey(usuario, models.CASCADE, related_name='usuario_envia')
    UsuarioRecebe = models.ForeignKey(usuario, models.CASCADE, related_name='usuario_recebe')

    class Meta:
        db_table = 'notificacao'