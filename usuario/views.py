from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import usuario

# Create your views here.

@login_required(login_url='/login/')
def register_usuario(request):
    return render(request, 'register.html')

@login_required(login_url='/login/')
def set_usuario(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    foto = request.FILES.get('file')
    user = request.user
    usuario1 = usuario.objects.create(email=email, nome=nome, senha=senha, foto=foto, user=user)
    return redirect("/")

@login_required(login_url='/login/')
def list_all_usuario(request):#listando os usuarios
    user = usuario.objects.filter(active=True)
    #print(user.query)
    return render(request, 'list.html', {'user': user})#passando um dicionario

def list_user_usuario(request):
    user = usuario.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'user': user})

def logout_user(request):
    logout(request)
    return redirect('/login/')
def login_user(request):
    return  render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print('username')
        #print('password')
        user = authenticate(username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválido. Favor tentar novamente')
        return redirect('/login/')
