from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.forms import AutosFormulario
from AppCoder.models import Autos
from AppCoder.models import Curso


def inicio(request):
    return render (request , "appcoder/inicio.html")

def cursos(request):
    lista_curso = Curso.objects.all()
    return render(request,"appcoder/cursos.html",{"cursos":lista_curso})

def profesores(request):
     return render(request,"appcoder/profesores.html")

def estudiantes(request):
     return render(request,"appcoder/estudiantes.html")

def entregables(request):
     return render(request,"appcoder/entregables.html")

def Autos(request):
    Lista_Autos = Autos.objects.all()
    return render(request,"appcoder/Autos.html",{"Autos":Lista_Autos})

def Sucursales(request):
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