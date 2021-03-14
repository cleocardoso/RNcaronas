
from notificacoes.models import notificacao
from usuario.models import usuario

def show_notificacoes(request):
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    sql = "SELECT * from notificacao n " \
          "inner join usuario u on(u.id = n.UsuarioEnvia_id) " \
          "inner join usuario u2 on(u2.id = n.UsuarioRecebe_id) " \
          "where u.id = %s or u2.id = %s limit 3"
    return notificacao.objects.raw(sql, [usuario2.id, usuario2.id])

def list_notificacoes(request):
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    sql = "SELECT * from notificacao n " \
          "inner join usuario u on(u.id = n.UsuarioEnvia_id) " \
          "inner join usuario u2 on(u2.id = n.UsuarioRecebe_id) " \
          "where u.id = %s or u2.id = %s"
    return notificacao.objects.raw(sql, [usuario2.id, usuario2.id])