from django.urls import path

from notificacoes import views


urlpatterns = [
    path('', views.list),
]