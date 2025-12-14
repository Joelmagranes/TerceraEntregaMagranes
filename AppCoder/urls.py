
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Autos/', views.Autos_view, name="Autos"),
    path('Sucursales/',views.Sucursales_view, name="Sucursales"),
    path('Ventas/', views.Ventas, name="Ventas"),
    path( 'AutosFormulario/', views.Cargar_auto, name="AutosFormulario"),
    path( 'SucursalesFormulario/', views.Cargar_sucursal, name="SucursalesFormulario"),
    path( 'busquedamodelo/', views.busquedamodelo, name="busquedacamada"),
    path('buscar/',views.buscar),
    path('buscarsucursal/',views.buscarsucursal, name="buscarsucursal"),
    path('busquedasucursal/', views.busquedasucursal, name="FormularioSucursal"),
    ]
