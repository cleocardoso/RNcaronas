from django.urls import path

from Relatorio import views


urlpatterns = [
    path('relatorio/relatorio', views.indexRelatorio),
    path('relatorio/relatorio/submit', views.set_relatorio_ofCarona, name="setRelatorio"),
    path('relatorio/pedir/relatorio/submit', views.set_relatorio_PedCarona, name="setRelatoriop"),
]