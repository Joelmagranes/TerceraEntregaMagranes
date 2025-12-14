from django.db import models

# Create your models here.
class Autos(models.Model):
    marca=models.CharField(max_length=40)
    modelo=models.CharField(max_length=30)
    anio=models.IntegerField()
    color=models.CharField(max_length=15)
    precio=models.IntegerField()
class Sucursales(models.Model):
    ciudad=models.CharField(max_length=35)
    pais=models.CharField(max_length=15)
class Ventas(models.Model):
    autos=models.ForeignKey(Autos, on_delete=models.CASCADE)
    sucursales=models.ForeignKey(Sucursales, on_delete=models.CASCADE)
    fecha=models.DateField()