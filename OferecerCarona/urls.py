
from django.urls import path

from OferecerCarona import views


urlpatterns = [
    path('oferecerCarona/', views.oferecercarona, name="oferecercarona"),
    path('oferecerCarona/submit', views.set_oferecercarona),
    path('oferecerCarona/listOferecercarona', views.list_OferecerCarona),
    path('oferecerCarona/relatorio', views.indexRelatorio),
    path('oferecerCarona/relatorio/submit', views.set_relatorio_ofCarona, name="setRelatorio"),

]