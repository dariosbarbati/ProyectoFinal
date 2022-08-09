from django.contrib import admin

from django.contrib import admin
from Servicios.models import Meses

@admin.register(Meses)
class Meses_admin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'pagado', 'fecha']
