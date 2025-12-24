from django.http import HttpResponse
from django.shortcuts import redirect, render

from AppFinal.forms import AutosFormulario, SucursalesFormulario
from AppFinal.models import Autos, Avatar
from AppFinal.models import Sucursales
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import AvatarForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin




def inicio(request):
    return render (request , "AppFinal/inicio.html")
def Autos_view(request):
    Lista_Autos = Autos.objects.all()
    return render(request,"AppFinal/Autos.html",{"autos":Lista_Autos})

def Sucursales_view(request):
     Lista_Sucursales = Sucursales.objects.all()
     return render(request, "AppFinal/Sucursales.html", {"sucursales": Lista_Sucursales})

@login_required
def Ventas(request):
     return render( request,"AppFinal/Ventas.html")
@login_required
def Cargar_auto (request):
     if request.method == 'POST':
          miformulario=AutosFormulario(request.POST, request.FILES)
          print(miformulario)
          if miformulario.is_valid():
               informacion=miformulario.cleaned_data
               nuevo_auto = Autos(
                marca=informacion['marca'],
                modelo=informacion['modelo'],
                color=informacion['color'],
                anio=informacion['anio'],
                precio=informacion['precio'],
                imagen=informacion.get('imagen'),)
               nuevo_auto.save()
               return render (request, "AppFinal/inicio.html")
     else:
          miformulario=AutosFormulario()

     return render(request,"AppFinal/AutosFormulario.html", {"miformulario":miformulario})

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
               return render (request, "AppFinal/inicio.html")
     else:
          miformulario=SucursalesFormulario()
     return render(request,"AppFinal/sucursalesFormulario.html", {"miformulario":miformulario})

def busquedamodelo(request):
     return render (request, "AppFinal/busquedamodelo.html")

def buscar(request):
     if request.GET['modelo']:
          modelo=request.GET['modelo']
          autos=Autos.objects.filter(modelo__icontains=modelo)
          return render (request, "AppFinal/resultadobusqueda.html", {"autos":autos, "modelo":modelo})
     else:
          respuesta="No enviaste datos"
          return HttpResponse(respuesta)

def busquedasucursal(request):
     return render (request, "AppFinal/busquedasucursal.html")     

def buscarsucursal(request):
     if request.GET['ciudad']:
          ciudad=request.GET['ciudad']
          sucursales=Sucursales.objects.filter(ciudad__icontains=ciudad)
          return render (request, "AppFinal/resultadobusquedasucursal.html", {"sucursales":sucursales, "ciudad":ciudad})
     else:
          respuesta="No enviaste datos"
          return HttpResponse(respuesta)

@staff_member_required
def editar_auto(request, id):
    auto = Autos.objects.get(id=id)

    if request.method == "POST":
        form = AutosFormulario(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            auto.marca = info["marca"]
            auto.modelo = info["modelo"]
            auto.color = info["color"]
            auto.anio = info["anio"]
            auto.precio = info["precio"]
            if "imagen" in request.FILES:
                auto.imagen = request.FILES["imagen"]

            auto.save()
            return redirect("Autos")
    else:
        form = AutosFormulario(initial={
            "marca": auto.marca,
            "modelo": auto.modelo,
            "color": auto.color,
            "anio": auto.anio,
            "precio": auto.precio,
        })

    return render(request, "AppFinal/AutosFormulario.html", {"miformulario": form, "auto": auto})

@staff_member_required
def eliminar_auto(request, id):
    auto = Autos.objects.get(id=id)
    auto.delete()
    return redirect("Autos")


#crecion de vistas para login y register

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'AppFinal/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data.get("admin_key") == "Coderhouse":
            user.is_staff = True
        user.save()
        return super().form_valid(form)


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST, instance=usuario)

        if formulario.is_valid():
            formulario.save()
            return render(request, "AppFinal/inicio.html")

    else:
        formulario = UserEditForm(instance=usuario)

    return render(
        request,
        "AppFinal/editar_perfil.html",
        {"miFormulario": formulario, "usuario": usuario},
    )

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'AppFinal/cambiar_contrasenia.html'
    success_url = reverse_lazy('EditarPerfil')

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            avatar = Avatar.objects.filter(user=request.user)
            if avatar.exists():
                avatar.delete()

            nuevo_avatar = Avatar(user=request.user, imagen=form.cleaned_data['imagen'])
            nuevo_avatar.save()

            return render(request, "AppFinal/inicio.html")

    else:
        form = AvatarForm()

    return render(request, "AppFinal/agregar_avatar.html", {"form": form})

class AboutView(TemplateView):
    template_name = "AppFinal/about.html"

class SucursalDeleteView(UserPassesTestMixin, DeleteView):
    model = Sucursales
    template_name = "AppFinal/borrarsucursales.html"
    success_url = reverse_lazy("Sucursales")

    def test_func(self):
        return self.request.user.is_staff
