from django.urls import path
from Servicios.views import lista_meses, actualizar_mes,\
lista_meses_admin, buscar_mes, ver_pagos, info_mes, agregar_servicio, agregar_usuario


urlpatterns = [
    path('administrador/', lista_meses_admin, name='actualizar-mes'),
    path('lista/', lista_meses, name= "listar_meses"),
    path('actualizar-mes/<int:pk>/', actualizar_mes, name='actualizar-mes'),
    path('buscar-mes/', buscar_mes, name='buscar-mes'),
    path('ver-pagos/', ver_pagos, name='buscar-mes'),
    path('info-mes/<int:pk>/', info_mes, name='info-mes'),
    path('agregar-servicio/', agregar_servicio, name='agregar-servicio'),
    path('agregar-usuario/', agregar_usuario, name='agregar-usuario'),
]
