from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from rest_framework import viewsets

from OferecerCarona.models import oferecerCarona
from PedirCarona.models import pedirCarona
from PedirCarona.serializers import PedCaronaSerializer

from usuario.models import usuario
from Carona.models import Carona
from notificacoes.models import notificacao


class pedirCaronaViewSet(viewsets.ModelViewSet):
    queryset = pedirCarona.objects.all()
    serializer_class = PedCaronaSerializer


def pedir_Carona(request):
    sql = "SELECT * from pedir_carona p " \
          "inner join usuario u on(u.id = p.usuario_id) " \
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
    ofCarona = oferecerCarona.objects.get(id=carona.oferecer_carona.id)
    if carona:
        ofCarona.quantidadeVagas -= int(quantidade)
        if ofCarona.quantidadeVagas >= 0:
            pedCarona = pedirCarona.objects.create(dataPedCarona=datetime.now(), quantidadeVagas=quantidade, carona=carona
                                                   , usuario=usuario2)
            pedCarona.statusAndamento = True
            pedCarona.save()
            ofCarona.save()

            # usuario envia o pedido: pedCarona.Usuario
            # usuario recebe a notificacao: carona.oferecerCarona.Usuario
            set_notificacao(datetime.now(), "Pedido Solicitado", pedCarona.usuario, carona.oferecer_carona.usuario, pedCarona)
            messages.success(request, 'Pedido de carona efetuado com sucesso!')
        else:
            messages.error(request, 'Quantidade Insuficiente!')
    return redirect('/usurious/index')


def aceitaPedido(request, id):
    pedir = pedirCarona.objects.get(id=id)
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)

    if pedir:
        pedir.statusConcluido = True
        pedir.statusAndamento = False
        oferecer = pedir.carona.oferecer_carona
        oferecer.valor_total -= int(oferecer.valorCarona) * int(pedir.quantidadeVagas)
        oferecer.save()
        pedir.total = int(oferecer.valorCarona) * int(pedir.quantidadeVagas)
        print(pedir.total)
        pedir.save()
        set_notificacao(datetime.now(), "Pedido Aceito", usuario2, pedir.usuario, pedir)
        messages.success(request, 'Pedido aceito com sucesso!')
    return redirect('/pedCaronas/pedirCarona/listPedidoSolicitado')

def recusarPedido(request, id):
    pedir = pedirCarona.objects.get(id=id)
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)

    if pedir:
        pedir.statusCancelado = True
        pedir.statusAndamento = False
        pedir.save()
        set_notificacao(datetime.now(), "Pedido Recusado!", usuario2, pedir.usuario, pedir)
        #messages.success(request, 'Pedido aceito com sucesso!')
    return redirect('/pedCaronas/pedirCarona/listPedidoSolicitado')

def listPedSolicitado(request):
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)

    sqlPd = "SELECT * from pedir_carona ofc " \
            "inner join carona c on(ofc.carona_id = c.id) " \
            "inner join oferecer_carona cf on(cf.id = c.oferecer_carona_id) " \
            "inner join usuario u on(u.id = cf.usuario_id) " \
            "where u.id = %s  and  ofc.statusAndamento = 1 and ofc.statusCancelado = 0 "

    caronasPd = pedirCarona.objects.raw(sqlPd, [usuario2.id])

    return render(request, 'listaPedidoSolicitados.html', {'ListPedidos': caronasPd})



def set_notificacao(data, mgs, usuario_envia, usuario_recebe, pedido):
    notificacao.objects.create(data=data, mensagem=mgs, usuario_envia=usuario_envia,
                               usuario_recebe=usuario_recebe, pedido_solicitado=pedido)
    return
