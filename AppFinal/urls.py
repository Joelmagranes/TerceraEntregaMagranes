
from django.urls import include, path
from AppFinal import views
from .views import AboutView, Autos_view, CambiarContrasenia, Cargar_auto, RegisterView, SucursalDeleteView, editar_auto, eliminar_auto
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

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
    path("editarPerfil/", views.editarPerfil, name="EditarPerfil"),
    ]

url_vistas_clases = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(
        template_name='AppFinal/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(template_name='AppFinal/logout.html'), name='logout'),
    path('cambiarContrasenia/', CambiarContrasenia.as_view(), name="CambiarContrasenia"),
    path('agregarAvatar/', views.agregarAvatar, name="AgregarAvatar"),
    path('about/', AboutView.as_view(), name="About"),
    path('sucursal/eliminar/<int:pk>/', SucursalDeleteView.as_view(), name="EliminarSucursal"),

]

urlpatterns += url_vistas_clases
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
