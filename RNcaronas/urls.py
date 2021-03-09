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
from usuario import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from usuario.views import usuarioViewSet, oferecerCaronaViewSet, pedirCaronaViewSet
from . import settings

router = routers.DefaultRouter()
router.register(r'usurious', usuarioViewSet)
router.register(r'ofCaronas', oferecerCaronaViewSet)
router.register(r'pedCaronas', pedirCaronaViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('usuario-auth/', include('rest_framework.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    path('admin/', admin.site.urls),
    path('usurious/list', views.list_all_usurious),
    path('usurious/user', views.list_user_usurious),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('usurious/register', views.register_usurious),
    path('usurious/register/submit', views.set_usurious),
    path('usurious/oferecerCarona/', views.oferecercarona_usurious),
    path('usurious/oferecerCarona/submit', views.set_oferecercarona_usurious),
    path('usurious/listOferecercarona', views.list_OferecerCarona),
    path('usurious/index', views.index_usurious, name="index"),
    path('usurious/index/submit', views.set_index_usurious),
    path('', RedirectView.as_view(url='usurious/index'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
