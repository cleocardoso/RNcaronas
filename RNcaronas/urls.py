"""RNcaronas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Carona.views import CaronaViewSet
from OferecerCarona import urls as oferecerCarona_url
from Relatorio import urls as relatorio_url
from usuario import urls as usuario_url
from PedirCarona import urls as pedirCarona_url
from notificacoes import urls as notificacao_url
from usuario import views

from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from rest_framework_swagger.views import get_swagger_view
from usuario.views import usuarioViewSet
from OferecerCarona.views import oferecerCaronaViewSet
from PedirCarona.views import pedirCaronaViewSet

from . import settings


router = routers.DefaultRouter()
router.register(r'usurious', usuarioViewSet, basename='usuario')
router.register(r'ofCaronas', oferecerCaronaViewSet, basename='OferecerCarona')
router.register(r'pedCaronas', pedirCaronaViewSet, basename='PedirCarona')
router.register(r'Caronas', CaronaViewSet, basename='Carona')

schema_view = get_swagger_view(title='API RNcaronas')

urlpatterns = [
    path('api/', include(router.urls)),
    path('usuario-auth/', include('rest_framework.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('usurious/', include(usuario_url)),
    path('ofCaronas/', include(oferecerCarona_url)),
    path('pedCaronas/', include(pedirCarona_url)),
    path('relatorio/', include(relatorio_url)),
    path('notificacao/', include(notificacao_url)),
    path('swagger/', schema_view),
    #path('oferecerCarona/submit', oferecerCaronaViewSet.set_oferecercarona),
    #path('oferecerCarona/listOferecercarona', oferecerCaronaViewSet.list_OferecerCarona),

    path('', RedirectView.as_view(url='usurious/index'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
