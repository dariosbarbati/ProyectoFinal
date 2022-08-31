from datetime import date
from lib2to3.pgen2 import token
from re import search
from django.shortcuts import render, redirect
from Servicios.models import Meses, Servicios
from Servicios.form import Formulario_servicio, Formulario_mes
from django.utils.crypto import get_random_string
listameses=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]

def lista_meses(resquest):
    data=Meses.objects.all()
    data2=Servicios.objects.all()
    context={"meses": data, "servicios": data2}
    return  render(resquest,"administrador-mes.html",context=context) 


def lista_meses_admin(request):
    data=Meses.objects.all()
    data2=Servicios.objects.all()
    context={"meses": data[0:12], "servicios": data2}  #DEVUELVO UNICAMENTE LOS PRIMEROS 12 MESES
    return  render(request,"administrador-mes.html",context=context) 

def lista_meses_admin_mes(request,pk):
    data=Meses.objects.filter(MesesServicio= pk)
    data2=Servicios.objects.all()
    data3=Servicios.objects.filter(id= pk)
    print(data3)
    context={"activo": data3, "meses": data, "servicios": data2 }
    return  render(request,"administrador-mes.html",context=context) 


def actualizar_mes(request, pk):
    if request.method == 'POST':
        form = Formulario_mes(request.POST)
        if form.is_valid():
            mes = Meses.objects.get(id=pk)
            mes.precio = form.cleaned_data['precio']
            mes.pagado = form.cleaned_data['pagado']
            mes.fecha = form.cleaned_data['fecha']
            if mes.pagado :
                mes.aleatorio = get_random_string(length=30)
            else:
                mes.aleatorio = 0               
            mes.save()
            return redirect(lista_meses_admin)

    elif request.method == 'GET':
        meses = Meses.objects.get(id=pk)

        form = Formulario_mes(initial={
            'nombre':meses.nombre,
            'precio':meses.precio, 
            'pagado':meses.pagado,
            'fecha':meses.fecha,  
            'token':meses.aleatorio,                       
            })
        context = {'form':form}
        return render(request, 'actualizar-mes.html', context=context)

def buscar_mes(request):
    search = request.GET['search']
    data = Meses.objects.filter(nombre__icontains=search)  
    context = {'mes':data}
    return render(request, 'buscar-mes.html', context=context)

def ver_pagos(request):
    data=Meses.objects.all()
    data2=Servicios.objects.all()
    context={"meses": data, "servicios": data2}
    return render(request, 'ver-pagos.html', context=context)

def ver_servicios(request):
    dato=Servicios.objects.all()
    context={"servicios": dato}
    return render(request, 'lista-eliminar-servicio.html', context=context)

def info_mes(request, pk):
    if request.method == 'GET':
        meses = Meses.objects.get(id=pk)

        form = Formulario_mes(initial={
        'nombre':meses.nombre,
        'precio':meses.precio, 
        'pagado':meses.pagado,
        'fecha':meses.fecha,
        'token':meses.aleatorio,            
        })
        context = {'form':form}
        return render(request, 'info-mes.html', context=context)


def agregar_servicio(request):
    if request.method == 'POST':
        form = Formulario_servicio(request.POST)
        if form.is_valid():
            s = Servicios.objects.create(
                servicio = form.cleaned_data['servicio'],
                precio = form.cleaned_data['precio'],
                descripcion = form.cleaned_data['descripcion'],
                habilitar = form.cleaned_data['habilitar']
            )
            for listames in listameses:
                m = Meses.objects.create(
                nombre = listames,
                precio = 0,
                pagado = False,
                fecha = date.today(),
                aleatorio = 0,
                )
                m.MesesServicio = Servicios.objects.get(pk = s.id)
                m.save()

            return redirect(lista_meses_admin)

    if request.method == 'GET':
        form = Formulario_servicio()
        context = {'form':form}
        return render(request, 'agregar-servicio.html', context=context)


def en_construccion (request):
    return render(request , "en-construccion.html", context={})

def eliminar_servicio(request,pk):
    if request.method == 'POST':
            servicio = Servicios.objects.get(pk=pk)
            servicio.delete()         
            return redirect(lista_meses_admin)

    if request.method == 'GET':
        dato=Servicios.objects.get(id=pk)
        context={"servicio": dato}
        print("por get")   
        return render(request, 'eliminar-servicio.html', context=context)