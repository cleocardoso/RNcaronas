import bcrypt
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import serializers
from rolepermissions.roles import assign_role
from rest_framework.authtoken.models import Token
from .models import usuario, pedirCarona
from .models import oferecerCarona

# Create your views here.
from .serializers import usuarioSerializer, oferecerCaronaSerializer, pedirCaronaSerializer


class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer

class oferecerCaronaViewSet(viewsets.ModelViewSet):
    queryset = oferecerCarona.objects.all()
    serializer_class = oferecerCaronaSerializer

class pedirCaronaViewSet(viewsets.ModelViewSet):
    queryset = pedirCarona.objects.all()
    serializer_class = pedirCaronaSerializer





#@login_required(login_url='/login/')
## essa anotação terá acesso a rota se realizar o login
def register_usurious(request):
    return render(request, 'register.html')

@login_required(login_url='/login/')
def oferecercarona_usurious(request):
    return render(request, 'oferecerCarona.html')


#@login_required(login_url='/login/')
def set_usurious(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    nrTelCelular = request.POST.get('nrTelCelular')
    foto = request.FILES.get('file')
    #hashed = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())
    #print(nome, email, senha)


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
def set_oferecercarona_usurious(request):
    dataOfCarona = request.POST.get('dataOfCarona')
    destino = request.POST.get('destino')
    partida = request.POST.get('partida')
    quantidadeVagas = request.POST.get('quantidadeVagas')
    valorCarona = request.POST.get('valorCarona')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    #print("usuario logado = ",usuario2)
    #print(dataOfCarona, destino, partida, quantidadeVagas, valorCarona)
    res = oferecerCarona.objects.create(dataOfCarona=dataOfCarona, destino=destino, partida=partida,  quantidadeVagas=quantidadeVagas, valorCarona=valorCarona, usuario=usuario2)

    res.save()
    
    return redirect('/usurious/listOferecercarona')

def list_OferecerCarona(request):#listando os usuarios
    ofcarona = oferecerCarona.objects.filter()
    #print(oferecerCarona.query)
    print("Passando aqui..")
    return render(request, 'listOferecerCarona.html', {'ofcarona': ofcarona})

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
    List = oferecerCarona.objects.all()

    #realizando a busca e filtrando na tabela
    destino = request.GET.get('destino')
    partida = request.GET.get('partida')
    data = request.GET.get('dataPedCarona')
    if destino and partida:
        print("DESTINO "+destino, "PARTIDA "+partida)
        List = List.filter(destino__icontains=destino) & List.filter(
            partida__icontains=partida) & List.filter(dataOfCarona=data)

    #print(destino)
    print(List)
    return render(request, 'index.html', {'List': List})

def set_index_usurious(request):
    dataPedCarona = request.POST.get('dataPedCarona')
    destino = request.POST.get('destino')
    partida = request.POST.get('partida')
    quantidadeVagas = request.POST.get('quantidadeVagas')
    usuario3 = request.user
    usuario2 = usuario.objects.get(email=usuario3.email)
    result = pedirCarona.objects.create(dataPedCarona=dataPedCarona, destino=destino, partida=partida, quantidadeVagas=quantidadeVagas, usuario=usuario2)
    print(result)

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

