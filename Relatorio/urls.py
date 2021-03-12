from django.urls import path

from Relatorio import views


urlpatterns = [
    path('oferecerCarona/relatorio', views.list_CarnonasData),
    path('', views.index, name='relatorio'),
]