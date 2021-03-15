from django.contrib import admin

# Register your models here.
from PedirCarona.models import pedirCarona


@admin.register(pedirCarona)
class PedirCaronaAdmin(admin.ModelAdmin):
   list_display = ['id', 'quantidade_vagas']
