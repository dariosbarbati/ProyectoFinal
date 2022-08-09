from django.db import models

class Meses(models.Model):
    nombre = models.CharField(max_length=40,null=True,blank=True)
    precio=models.FloatField()
    pagado=models.BooleanField(default=False)
    fecha= models.DateField (auto_now=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Mes'
        verbose_name_plural = 'Meses'


class Servicios(models.Model):
    servicio = models.CharField(max_length=40)
    precio = models.FloatField()
    descripcion =  models.CharField(max_length=40)
    habilitar = models.BooleanField(default=False)

    def __str__(self):
        return self.servicio