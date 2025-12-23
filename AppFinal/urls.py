
from django.urls import path
from AppFinal import views
from .views import Autos_view, Cargar_auto, RegisterView, editar_auto, eliminar_auto
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

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
    path("Autos/", Autos_view, name="Autos"),
    path("Autos/agregar/", Cargar_auto, name="AutosAgregar"),
    path("Autos/editar/<int:id>/", editar_auto, name="AutosEditar"),
    path("Autos/eliminar/<int:id>/", eliminar_auto, name="AutosEliminar"),
    ]

url_vistas_clases = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(
        template_name='AppFinal/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(template_name='AppFinal/logout.html'), name='logout'),
]

urlpatterns += url_vistas_clases