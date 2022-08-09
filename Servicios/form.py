from django import forms


class Formulario_mes(forms.Form):
    nombre = forms.CharField(max_length=40) #, disabled=True
    precio = forms.FloatField()
    fecha = forms.DateField()
    pagado = forms.BooleanField(required=False)

class Formulario_servicio(forms.Form):
    servicio = forms.CharField(max_length=40) 
    precio = forms.FloatField()
    descripcion =  forms.CharField(max_length=40)
    habilitar = forms.BooleanField(required=False)

class Formulario_usuario(forms.Form):
    usuario = forms.CharField(max_length=40) 
    contrasena = forms.CharField(max_length=40)
    mail = forms.EmailField()
    habilitar = forms.BooleanField(required=False)



