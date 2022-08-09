from django.shortcuts import render, redirect
from Servicios.models import Meses, Servicios
from Servicios.form import Formulario_mes
from Servicios.form import Formulario_servicio


def lista_meses(resquest):
    data=Meses.objects.all()
    data2=Servicios.objects.all()
    context={"meses": data, "servicios": data2}
    return  render(resquest,"usuario.html",context=context) 


def lista_meses_admin(request):
    data=Meses.objects.all()
    data2=Servicios.objects.all()
    context={"meses": data, "servicios": data2}
    return  render(request,"administrador.html",context=context) 


def actualizar_mes(request, pk):
    if request.method == 'POST':
        form = Formulario_mes(request.POST)
        if form.is_valid():
            mes = Meses.objects.get(id=pk)
            # mes.nombre = form.cleaned_data['nombre']
            mes.precio = form.cleaned_data['precio']
            mes.pagado = form.cleaned_data['pagado']
            mes.fecha = form.cleaned_data['fecha']
            mes.save()

            return redirect(lista_meses_admin)


    elif request.method == 'GET':
        meses = Meses.objects.get(id=pk)

        form = Formulario_mes(initial={
            'nombre':meses.nombre,
            'precio':meses.precio, 
            'pagado':meses.pagado,
            'fecha':meses.fecha,            
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

def info_mes(request, pk):
    if request.method == 'GET':
        meses = Meses.objects.get(id=pk)

        form = Formulario_mes(initial={
        'nombre':meses.nombre,
        'precio':meses.precio, 
        'pagado':meses.pagado,
        'fecha':meses.fecha,            
        })
        context = {'form':form}
        return render(request, 'info-mes.html', context=context)


def agregar_servicio(request):
    if request.method == 'POST':
        form = Formulario_servicio(request.POST)
        if form.is_valid():
            Servicios.objects.create(
                servicio = form.cleaned_data['servicio'],
                precio = form.cleaned_data['precio'],
                descripcion = form.cleaned_data['descripcion'],
                habilitar = form.cleaned_data['habilitar']
            )
            return redirect(lista_meses_admin)


    if request.method == 'GET':
        form = Formulario_servicio()
        context = {'form':form}
        return render(request, 'agregar-servicio.html', context=context)