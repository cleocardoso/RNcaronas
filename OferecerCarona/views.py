from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets

from OferecerCarona.models import oferecerCarona
from OferecerCarona.serializers import oferecerCaronaSerializer
from usuario.models import usuario
from Carona.models import Carona

from notificacoes.util import show_notificacoes


class oferecerCaronaViewSet(viewsets.ModelViewSet):
    queryset = oferecerCarona.objects.all()
    serializer_class = oferecerCaronaSerializer


@login_required(login_url='/login/')
def oferecercarona(request):
    return render(request, 'oferecerCarona.html')


@login_required(login_url='/login/')
def set_oferecercarona(request):
    dataOfCarona = request.POST.get('dataOfCarona')
    destino = request.POST.get('destino')
    partida = request.POST.get('partida')
    quantidadeVagas = request.POST.get('quantidadeVagas')
    valorCarona = request.POST.get('valorCarona')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    total = int(valorCarona) * int(quantidadeVagas)
    res = oferecerCarona.objects.create(data_carona=dataOfCarona, quantidade_vagas=quantidadeVagas,
                                        valor_carona=valorCarona, valor_total=total, usuario=usuario2)
    res.save()
    carona = Carona.objects.create(destino=destino, partida=partida, oferecer_carona=res)
    carona.save()
    messages.success(request, 'Carona adicionada com sucesso!')
    return redirect('/ofCaronas/oferecerCarona/listOferecercarona')


@login_required(login_url='/login/')
def list_OferecerCarona(request):  # listando os usuarios
    # retornar as minhas caronas
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    sql = "SELECT * from carona c inner join oferecer_carona ofc on(c.oferecer_carona_id = ofc.id) " \
          "inner join usuario u on(u.id = ofc.usuario_id) where u.id = %s"
    caronas = Carona.objects.raw(sql, [usuario2.id])
    return render(request, 'listOferecerCarona.html', {'caronas': caronas, 'notificacoes': show_notificacoes(request)})



