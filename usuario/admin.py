from django.contrib import admin
from .models import usuario
from .models import oferecerCarona
from .models import pedirCarona

# Register your models here.
@admin.register(usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'senha']

@admin.register(oferecerCarona)
class OferecerCaronaAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario']

@admin.register(pedirCarona)
class PedirCaronaAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario']
