from django import forms


class Formulario_mes(forms.Form):
    nombre = forms.CharField(max_length=40) #, disabled=True
    precio = forms.FloatField()
    pagado = forms.BooleanField(required=False)
    fecha = forms.DateField()
    token = forms.CharField(max_length=30,required=False)

class Formulario_servicio(forms.Form):
    servicio = forms.CharField(max_length=40) 
    precio = forms.FloatField()
    descripcion =  forms.CharField(max_length=40,required=False)
    habilitar = forms.BooleanField(required=False)





