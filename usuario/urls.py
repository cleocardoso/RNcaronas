from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from usuario import views


urlpatterns = [
    path('list', views.list_all_usurious),
    path('user', views.list_user_usurious),
    path('register', views.register_usurious),
    path('register/submit', views.set_usurious),
    path('index', views.index_usurious, name="index"),
    path('index/submit', views.set_index_usurious),
]