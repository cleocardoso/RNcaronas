from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from .models import usuario
from Carona.models import Carona

from PedirCarona.models import pedirCarona
# Create your views here.
from .serializers import usuarioSerializer


# from .models import oferecerCarona
class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer

#@login_required(login_url='/login/')
## essa anotação terá acesso a rota se realizar o login
def register_usurious(request):
    return render(request, 'register.html')






#@login_required(login_url='/login/')
def set_usurious(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    nrTelCelular = request.POST.get('nrTelCelular')
    foto = request.FILES.get('file')



    new_user = User.objects.filter(username=email)
    # verificar se existe alguem com esse email, la na tabela auth_user.
    # Se  retorna true  vai retornar a mensagem de erro, caso contrario ele vai salvar

    if not new_user:
        user = User(username=email, first_name=nome,
                    last_name="", email=email)
        user.set_password(senha)
        user.save()
        userT = usuario(email=email, nome=nome, senha=senha, foto=foto, user=user, nrTelCelular=nrTelCelular)

        userT.save()
        #Token.objects.create(user=user)

        return redirect("/usurious/list")
    messages.error(request, 'E-mail já cadastrado. Por favor tente outro')

    # aqui  retonar o usuario, para ele apenas mudar o email
    return redirect('/usurious/register')

@login_required(login_url='/login/')
def list_all_usurious(request):#listando os usuarios
    user = usuario.objects.filter(active=True)
    print(user.query)
    return render(request, 'list.html', {'user': user})#passando um dicionario

def list_user_usurious(request):
    user = usuario.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'user': user})

def logout_user(request):
    logout(request)
    return redirect('/login/')
def login_user(request):
    return render(request, 'login.html')

def index_usurious(request):
    # query nativa
    query = "select * from Carona c inner join oferecerCarona o on(c.oferecerCarona_id = o.id) " \
            "where o.quantidadeVagas > 0 and c.destino = %s  and " \
            "c.partida = %s and o.dataOfCarona = %s "
    List = None

    #realizando a busca e filtrando na tabela
    destino = request.GET.get('destino')
    partida = request.GET.get('partida')
    data = request.GET.get('dataPedCarona')

    if destino and partida and data:
        List = Carona.objects.raw(query, [destino, partida, data])
    return render(request, 'index.html', {'List': List})


def set_index_usurious(request):
    dataPedCarona = request.POST.get('dataPedCarona')
    destino = request.POST.get('destino')
    partida = request.POST.get('partida')
    quantidadeVagas = request.POST.get('quantidadeVagas')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    result = pedirCarona.objects.create(dataPedCarona=dataPedCarona, destino=destino, partida=partida, quantidadeVagas=quantidadeVagas, usuario=usuario2)


    result.save()

    return redirect('usurious/index')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username)
        #print(password)
        user = authenticate(username=username, password=password)
        #print(user)


        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválido. Favor tentar novamente')
        return redirect('/login/')

