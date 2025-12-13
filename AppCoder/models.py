from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
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