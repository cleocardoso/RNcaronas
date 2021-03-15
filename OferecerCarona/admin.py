from django.contrib import admin

# Register your models here.
from OferecerCarona.models import oferecerCarona


@admin.register(oferecerCarona)
class OferecerCaronaAdmin(admin.ModelAdmin):
    list_display = ['id', 'valor_carona']