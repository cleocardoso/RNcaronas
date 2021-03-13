from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from rest_framework import viewsets

from OferecerCarona.models import oferecerCarona
from PedirCarona.models import pedirCarona

from usuario.models import usuario
from Carona.models import Carona
from notificacoes.models import notificacao


class pedirCaronaViewSet(viewsets.ModelViewSet):
    queryset = pedirCarona.objects.all()
    serializer_class = pedirCarona

def pedir_Carona(request):
    sql = "SELECT * from pedirCarona p " \
          "inner join usuario u on(u.id = p.Usuario_id) " \
          "where u.id = %s"
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    pedidos = pedirCarona.objects.raw(sql, [usuario2.id])
    return render(request, 'listPedirCarona.html', {'pedidos': pedidos})

def set_pedirCarona(request, id):
    #  metodo que vai confirmar o pedido da carona
    # enviar as informações da carona
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    quantidade = request.POST.get('quantidade')
    carona = Carona.objects.get(id=id)
    ofCarona = oferecerCarona.objects.get(id=carona.oferecerCarona.id)
    if carona:
        ofCarona.quantidadeVagas -= int(quantidade)
        if ofCarona.quantidadeVagas >= 0:
            pedCarona = pedirCarona.objects.create(dataPedCarona=datetime.now(), quantidadeVagas=quantidade, carona=carona
                                                   , Usuario=usuario2)
            pedCarona.save()
            ofCarona.save()
            # usuario envia o pedido: pedCarona.Usuario
            # usuario recebe a notificacao: carona.oferecerCarona.Usuario
            set_notificacao(datetime.now(), "Pedido Solicitado", pedCarona.Usuario, carona.oferecerCarona.Usuario, pedCarona)
            messages.success(request, 'Pedido de carona efetuado com sucesso!')
        else:
            messages.error(request, 'Quantidade Insuficiente!')
    return redirect('/usurious/index')


"""def set_pedirCarona(request):
    dataPedCarona = request.POST.get('dataPedCarona')
    destino = request.POST.get('destino')
    partida = request.POST.get('partida')
    quantidadeVagas = request.POST.get('quantidadeVagas')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    res = oferecerCarona.objects.create(dataPedCarona=dataPedCarona, destino=destino, partida=partida,
                                            quantidadeVagas=quantidadeVagas, usuario=usuario2)

    res.save()
    # colocar uma mensagem de sucesso
    return redirect('/listPedirCarona')"""


def aceitaPedido(request, id):
    pedir = pedirCarona.objects.get(id=id)
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)

    if pedir:
        pedir.status = True
        pedir.save()
        set_notificacao(datetime.now(), "Pedido Aceito", usuario2, pedir.Usuario, pedir)

    return redirect('/pedCaronas/pedirCarona/listPedidoSolicitado')

def listPedSolicitado(request):
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)

    sqlPd = "SELECT * from pedirCarona ofc " \
            "inner join Carona c on(ofc.carona_id = c.id) " \
            "inner join oferecerCarona cf on(cf.id = c.oferecerCarona_id) " \
            "inner join usuario u on(u.id = cf.Usuario_id) " \
            "where u.id = %s  and  ofc.status = 0 "

    caronasPd = pedirCarona.objects.raw(sqlPd, [usuario2.id])

    return render(request, 'listaPedidoSolicitados.html', {'ListPedidos': caronasPd})



def set_notificacao(data, mgs, usuario_envia, usuario_recebe, pedido):
    notificacao.objects.create(data=data, mensagem=mgs, UsuarioEnvia=usuario_envia,
                               UsuarioRecebe=usuario_recebe, PedidoSolicidato=pedido)
    return
