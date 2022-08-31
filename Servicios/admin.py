from django.contrib import admin

from django.contrib import admin
from Servicios.models import Meses, Servicios

@admin.register(Meses)
class Meses_admin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'pagado', 'fecha', 'MesesServicio' ]

@admin.register(Servicios)
class Servicios_admin(admin.ModelAdmin):
    list_display = ['servicio', 'precio', 'descripcion', 'habilitar']

