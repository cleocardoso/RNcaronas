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
from .models import usuario
from .models import oferecerCarona

# Create your views here.
from .serializers import usuarioSerializer


class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer






@login_required(login_url='/login/')
def register_usurious(request):
    return render(request, 'register.html')

@login_required(login_url='/login/')
def set_usurious(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    foto = request.FILES.get('file')
    #user = request.user
    print(nome, email, senha)


    new_user = User.objects.filter(username=email)
    # esse new_user vai verificar se existe alguem com esse email, la na tabela auth_user.
    # Se tiver retorna true e vai retornar a mensagem de erro, caso contrario ele vai salvar

    if not new_user:
        user = User(username=email, first_name=nome,
                    last_name="", email=email)
        user.set_password(senha)
        user.save()
        userT = usuario(email=email, nome=nome, senha=senha, foto=foto, user=user)
        # usuario.objects.create(email=email, nome=nome, senha=senha, foto=foto, user=user)
        # usuario.user = user
        userT.save()
        #Token.objects.create(user=user)
        #assign_role(user, 'usuario') <- se quiser pode tirar
        return redirect("/usurious/list")
    messages.error(request, 'E-mail já cadastrado. Por favor tente outro')

    # aqui  retonar o usuario, para ele apenas mudar o email
    return redirect('/usurious/register')

def oferecercarona_usurious(request):
    dataOfCarona = request.POST.get('dataOfCarona')
    destino = request.POST.get('destino')
    partida = request.POST.get('partida')
    quantidadeVagas = request.POST.get('quantidadeVagas')
    valorCarona = request.POST.get('valorCarona')
    #usuario = request.usuario
    #print(dataOfCarona, destino, partida ,quantidadeVagas, valorCarona)
    res = oferecerCarona.objects.create(dataOfCarona=dataOfCarona, destino=destino, partida=partida,  quantidadeVagas=quantidadeVagas, valorCarona=valorCarona)
    return redirect("usurious/oferecerCarona")

def list_OferecerCarona(request):#listando os usuarios
    ofcarona = oferecerCarona.objects.filter()
    #print(oferecerCarona.query)
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
    return render(request, 'index.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválido. Favor tentar novamente')
        return redirect('/login/')
