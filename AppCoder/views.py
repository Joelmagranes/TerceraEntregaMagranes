from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.forms import AutosFormulario, SucursalesFormulario
from AppCoder.models import Autos
from AppCoder.models import Sucursales


def inicio(request):
    return render (request , "appcoder/inicio.html")
def Autos_view(request):
    Lista_Autos = Autos.objects.all()
    return render(request,"appcoder/Autos.html",{"Autos":Lista_Autos})

def Sucursales_view(request):
     return render(request, "appcoder/Sucursales.html")

def Ventas(request):
     return render( request,"appcoder/Ventas.html")

def Cargar_auto (request):
     if request.method == 'POST':
          miformulario=AutosFormulario(request.POST)
          print(miformulario)
          if miformulario.is_valid():
               informacion=miformulario.cleaned_data
               nuevo_auto = Autos(
                marca=informacion['marca'],
                modelo=informacion['modelo'],
                color=informacion['color'],
                anio=informacion['anio'],
                precio=informacion['precio'],)
               nuevo_auto.save()
               return render (request, "appcoder/inicio.html")
     else:
          miformulario=AutosFormulario()

     return render(request,"appcoder/AutosFormulario.html", {"miformulario":miformulario})

def Cargar_sucursal (request):
     if request.method == 'POST':
          miformulario=SucursalesFormulario(request.POST)
          print(miformulario)
          if miformulario.is_valid():
               informacion=miformulario.cleaned_data
               nueva_sucursal = Sucursales(
               ciudad=informacion['ciudad'],
               pais=informacion['pais'],)
               nueva_sucursal.save()
               return render (request, "appcoder/inicio.html")
     else:
          miformulario=SucursalesFormulario()
     return render(request,"appcoder/sucursalesFormulario.html", {"miformulario":miformulario})

def busquedamodelo(request):
     return render (request, "appcoder/busquedamodelo.html")

def buscar(request):
     if request.GET['modelo']:
          modelo=request.GET['modelo']
          autos=Autos.objects.filter(modelo__icontains=modelo)
          return render (request, "appcoder/resultadobusqueda.html", {"autos":autos, "modelo":modelo})
     else:
          respuesta="No enviaste datos"
          return HttpResponse(respuesta)

def busquedasucursal(request):
     return render (request, "appcoder/busquedasucursal.html")     

def buscarsucursal(request):
     if request.GET['ciudad']:
          ciudad=request.GET['ciudad']
          sucursales=Sucursales.objects.filter(ciudad__icontains=ciudad)
          return render (request, "appcoder/resultadobusquedasucursal.html", {"sucursales":sucursales, "ciudad":ciudad})
     else:
          respuesta="No enviaste datos"
          return HttpResponse(respuesta)
