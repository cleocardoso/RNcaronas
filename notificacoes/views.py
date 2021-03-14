from django.shortcuts import render
from rest_framework import viewsets

import notificacoes

from notificacoes.util import list_notificacoes


def list(request):
    return render(request,'notificacoes.html', {'notificacoes': list_notificacoes(request)})