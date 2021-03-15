from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuario.models import usuario
from Carona.models import Carona

# essa é de oferecer
def list_CarnonasData(request):
    dataOfCarona = request.POST.get('dataOfCarona')
    dataPedCarona = request.POST.get('dataPedCarona')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    sql = "SELECT * from Carona c inner join OferecerCarona ofc on(c.oferecerCarona_id = ofc.id)" \
          "inner join usuario u on(u.id = ofc.usuario_id) " \
          "where u.id = %s and ofc.dataOfCarona  BETWEEN %s  and %s"

    caronas = Carona.objects.raw(sql, [usuario2.id, dataOfCarona, dataPedCarona])

    return render(request, 'relatorio.html', {'caronas': caronas})


def set_relatorio_ofCarona(request):
    dataOfCarona = request.POST.get('dataOfCarona')
    dataPedCarona = request.POST.get('dataPedCarona')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    sqlOf = "SELECT * from Carona c inner join OferecerCarona ofc on(c.oferecerCarona_id = ofc.id)" \
            "inner join usuario u on(u.id = ofc.usuario_id) " \
            "where u.id = %s and ofc.dataOfCarona  BETWEEN %s  and %s"

    sqlPd = "SELECT * from Carona c inner join pedirCarona p on(c.id = p.carona_id)" \
            " inner join usuario u on(u.id = p.usuario_id) " \
            "where u.id = %s and p.dataPedCarona  BETWEEN %s  and %s"

    caronasOf = Carona.objects.raw(sqlOf, [usuario2.id, dataOfCarona, dataPedCarona])
    caronasPd = Carona.objects.raw(sqlPd, [usuario2.id, dataOfCarona, dataPedCarona])
    return render(request, 'relatorio.html', {'ListCarona': caronasOf, 'ListPedidos': caronasPd})


def set_relatorio_PedCarona(request):
    destino = request.POST.get('destino')
    partida = request.POST.get('partida')

    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)

    sqlPd = "SELECT * from Carona c inner join pedirCarona ofc on(ofc.carona_id = c.id)  " \
            " inner join usuario u on(u.id = ofc.usuario_id) " \
            "where u.id = %s and c.partida = %s and c.destino = %s and  ofc.statusConcluido = 1"

    sqlOf = "SELECT * from Carona c inner join OferecerCarona ofc on(c.oferecerCarona_id = ofc.id)" \
            "inner join usuario u on(u.id = ofc.usuario_id) " \
            "where u.id = %s and c.destino = %s and c.partida = %s"

    caronasOf = Carona.objects.raw(sqlOf, [usuario2.id, destino, partida])
    caronasPd = Carona.objects.raw(sqlPd, [usuario2.id, destino, partida])

    for ped in caronasPd:
        user = ped.oferecerCarona.Usuario
        print(user.nome)

    return render(request, 'relatorio.html', {'ListCarona': caronasOf, 'ListPedidos': caronasPd})


@login_required(login_url='/login/')
def indexRelatorio(request):
    return render(request, 'relatorio.html')
