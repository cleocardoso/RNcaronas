from django.shortcuts import render
from notificacoes.util import show_notificacoes, list_notificacoes


def list(request):
    return render(request,'notificacoes.html', {'notificacoes': list_notificacoes(request)})