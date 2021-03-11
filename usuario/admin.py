from django.contrib import admin
from .models import usuario


# Register your models here.
@admin.register(usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'senha']

