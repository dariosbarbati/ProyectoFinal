from tkinter import CASCADE
from django.db import models 


class Servicios(models.Model):
    servicio = models.CharField(max_length=40)
    precio = models.FloatField()
    descripcion =  models.CharField(max_length=40)
    habilitar = models.BooleanField(default=False)


    def __str__(self):
        return self.servicio

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'


class Meses(models.Model):
    nombre = models.CharField(max_length=40,null=True,blank=True)
    precio=models.FloatField()
    pagado=models.BooleanField(default=False)
    fecha= models.DateField (auto_now=False,null=True,blank=True)
    aleatorio = models.CharField(max_length=40,null=True,blank=True)
    MesesServicio=models.ForeignKey(Servicios, on_delete=models.CASCADE, related_name="MesesServicio",blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Mes'
        verbose_name_plural = 'Meses'   