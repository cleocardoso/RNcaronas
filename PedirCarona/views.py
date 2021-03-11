from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from rest_framework import viewsets

from OferecerCarona.models import oferecerCarona
from PedirCarona.models import pedirCarona

from usuario.models import usuario
from Carona.models import Carona

class pedirCaronaViewSet(viewsets.ModelViewSet):
    queryset = pedirCarona.objects.all()
    serializer_class = pedirCarona

def pedir_Carona(request):
    return render(request, 'index.html')

def test_carona(request, id):
    #  metodo que vai confirmar o pedido da carona
    # enviar as informações da carona
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    quantidade = request.POST.get('quantidade')
    carona = Carona.objects.get(id=id)
    ofCarona = oferecerCarona.objects.get(id=carona.oferecerCarona.id)
    if carona:
        ofCarona.quantidadeVagas -= int(quantidade)
        if ofCarona.quantidadeVagas > 0:
            pedCarona = pedirCarona.objects.create(dataPedCarona=datetime.now(), quantidadeVagas=quantidade, carona=carona
                                                   , Usuario=usuario2)
            pedCarona.save()
            ofCarona.save()
            messages.success(request, 'Pedido de carona efetuado com sucesso!')
        else:
            messages.error(request, 'Quantidade Insuficiente!')
    return redirect('/usurious/index')

def set_pedirCarona(request):
    dataPedCarona = request.POST.get('dataPedCarona')
    destino = request.POST.get('destino')
    partida = request.POST.get('partida')
    quantidadeVagas = request.POST.get('quantidadeVagas')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    res = oferecerCarona.objects.create(dataPedCarona=dataPedCarona, destino=destino, partida=partida,
                                            quantidadeVagas=quantidadeVagas, usuario=usuario2)

    res.save()

    return redirect('/listPedirCarona')



