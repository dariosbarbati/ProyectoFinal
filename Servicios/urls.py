from django.urls import path
from Servicios.views import lista_meses, actualizar_mes,\
lista_meses_admin, buscar_mes, ver_pagos, info_mes, agregar_servicio,\
lista_meses_admin_mes, en_construccion, eliminar_servicio, ver_servicios, about_us


urlpatterns = [
    path('administrador/', lista_meses_admin, name='actualizar-mes'),
    path('administrador-mes/<int:pk>/', lista_meses_admin_mes, name='actualizar-mes'),
    path('lista/', lista_meses, name= "listar_meses"),
    path('actualizar-mes/<int:pk>/', actualizar_mes, name='actualizar-mes'),
    path('buscar-mes/', buscar_mes, name='buscar-mes'),
    path('ver-pagos/', ver_pagos, name='buscar-mes'),
    path('info-mes/<int:pk>/', info_mes, name='info-mes'),
    path('agregar-servicio/', agregar_servicio, name='agregar-servicio'),
    path('en-construccion/', en_construccion, name='en-construccin'),
    path('lista-eliminar-servicio/', ver_servicios, name='lista-eliminar-servicio'),
    path('eliminar-servicio/<int:pk>/', eliminar_servicio, name='eliminar-servicio'),
    path('about-us/', about_us, name=('about_us'))
]
