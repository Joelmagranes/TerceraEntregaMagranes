
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),   # Nuestra primer view
    path('cursos/', views.cursos, name="Cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name="Entregables"),
    path('Autos/', views.Autos, name="Autos"),
    path('Sucursales/',views.Sucursales, name="Sucursales"),
    path('Ventas/', views.Ventas, name="Ventas"),
    path( 'AutosFormulario/', views.Cargar_auto, name="AutosFormulario"),
    path( 'SucursalesFormulario/', views.Cargar_sucursal, name="SucursalesFormulario"),
    path( 'busquedamodelo/', views.busquedamodelo, name="busquedacamada"),
    path('buscar/',views.buscar),
    path('buscarsucursal/',views.buscarsucursal, name="buscarsucursal"),
    path('busquedasucursal/', views.busquedasucursal, name="FormularioSucursal"),
    ]
