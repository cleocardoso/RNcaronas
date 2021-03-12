from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets

from OferecerCarona.models import oferecerCarona
from OferecerCarona.serializers import oferecerCaronaSerializer
from usuario.models import usuario
from Carona.models import Carona


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

    res = oferecerCarona.objects.create(dataOfCarona=dataOfCarona, quantidadeVagas=quantidadeVagas,
                                        valorCarona=valorCarona, Usuario=usuario2)
    res.save()
    carona = Carona.objects.create(destino=destino, partida=partida, oferecerCarona=res)
    carona.save()
    return redirect('/ofCaronas/oferecerCarona/listOferecercarona')


@login_required(login_url='/login/')
def list_OferecerCarona(request):  # listando os usuarios
    # retornar as minhas caronas
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    sql = "SELECT * from Carona c inner join oferecerCarona ofc on(c.oferecerCarona_id = ofc.id) " \
          "inner join usuario u on(u.id = ofc.Usuario_id) where u.id = %s"
    caronas = Carona.objects.raw(sql, [usuario2.id])

    print("Passando aqui..")
    return render(request, 'listOferecerCarona.html', {'caronas': caronas})


def set_relatorio_ofCarona(request):

    dataOfCarona = request.POST.get('dataOfCarona')
    dataPedCarona = request.POST.get('dataPedCarona')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    sqlOf = "SELECT * from Carona c inner join OferecerCarona ofc on(c.oferecerCarona_id = ofc.id)" \
         "inner join usuario u on(u.id = ofc.Usuario_id) " \
         "where u.id = %s and ofc.dataOfCarona  BETWEEN %s  and %s"
    sqlPd = "SELECT * from Carona c inner join pedirCarona p on(c.id = p.carona_id)" \
            " inner join usuario u on(u.id = p.Usuario_id) " \
            "where u.id = %s and p.dataPedCarona  BETWEEN %s  and %s"

    caronasOf = Carona.objects.raw(sqlOf, [usuario2.id, dataOfCarona, dataPedCarona])
    caronasPd = Carona.objects.raw(sqlPd, [usuario2.id, dataOfCarona, dataPedCarona])
    return render(request, 'relatorio.html', {'ListCarona': caronasOf, 'ListPedidos': caronasPd})

@login_required(login_url='/login/')
def indexRelatorio(request):
    print("passando ...")
    return render(request, 'relatorio.html')

