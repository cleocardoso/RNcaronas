from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuario.models import usuario
from Carona.models import Carona

@login_required(login_url='/login/')
def index(request):
    print(request)
    return render(request, 'relatorio.html')

# essa é de oferecer
def list_CarnonasData(request):

    dataOfCarona = request.POST.get('dataOfCarona')
    dataPedCarona = request.POST.get('dataPedCarona')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    sql= "SELECT * from Carona c inner join OferecerCarona ofc on(c.oferecerCarona_id = ofc.id)" \
         "inner join usuario u on(u.id = ofc.Usuario_id) " \
         "where u.id = %s and ofc.dataOfCarona  BETWEEN %s  and %s"

    caronas = Carona.objects.raw(sql, [usuario2.id, dataOfCarona, dataPedCarona])

    return render(request, 'relatorio.html', {'caronas': caronas})