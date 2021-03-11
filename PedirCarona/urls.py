from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from PedirCarona import views


urlpatterns = [
    path('pedirCarona/', views.pedir_Carona),
    path('pedirCarona/test/<str:id>', views.test_carona, name="test_carona"),
    path('pedirCarona/listPedirCarona', views.set_pedirCarona),
]