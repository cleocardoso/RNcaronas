from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from PedirCarona import views


urlpatterns = [
    path('', views.pedir_Carona),
    path('pedirCarona/test/<str:id>', views.set_pedirCarona, name="set_pedirCarona"),
    path('pedirCarona/listPedidoSolicitado', views.listPedSolicitado),
    path('pedirCarona/listPedidoSolicitado/submit/<str:id>',
         views.aceitaPedido, name='aceitar_pedido'),
]