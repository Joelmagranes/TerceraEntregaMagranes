from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autos(models.Model):
    marca=models.CharField(max_length=40)
    modelo=models.CharField(max_length=30)
    anio=models.IntegerField()
    color=models.CharField(max_length=15)
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='autos/', null=True, blank=True)
class Sucursales(models.Model):
    ciudad=models.CharField(max_length=35)
    pais=models.CharField(max_length=15)
class Ventas(models.Model):
    autos=models.ForeignKey(Autos, on_delete=models.CASCADE)
    sucursales=models.ForeignKey(Sucursales, on_delete=models.CASCADE)
    fecha=models.DateField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"
