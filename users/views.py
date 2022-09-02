from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Servicios.views import lista_meses_admin
from users.forms import User_registration_form


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # context = {'usuario': {user}}
                return redirect(lista_meses_admin) 

        form = AuthenticationForm()
        return render(request, 'login.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_request) 
        else:
            context = {'error':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'registrar.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'registrar.html', {'form': form})
