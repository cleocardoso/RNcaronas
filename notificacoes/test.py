
from notificacoes.models import notificacao

def show_notificacoes(request):
    id_usuario_logado = request.user.id
    sql = "SELECT * from notificacao n " \
          "inner join usuario u on(u.id = n.UsuarioEnvia_id) " \
          "inner join usuario u2 on(u2.id = n.UsuarioRecebe_id) " \
          "where u.id = %s or u2.id = %s"
    return notificacao.objects.raw(sql, [id_usuario_logado, id_usuario_logado])