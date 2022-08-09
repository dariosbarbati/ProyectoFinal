from django.contrib import admin

from django.contrib import admin
from Servicios.models import Meses, Servicios, Usuarios

@admin.register(Meses)
class Meses_admin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'pagado', 'fecha']

@admin.register(Servicios)
class Servicios_admin(admin.ModelAdmin):
    list_display = ['servicio', 'precio', 'descripcion', 'habilitar']

@admin.register(Usuarios)
class Usuarios_admin(admin.ModelAdmin):
    list_display = ['usuario', 'contrasena', 'mail', 'habilitar']
