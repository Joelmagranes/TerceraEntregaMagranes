from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AutosFormulario(forms.Form):
    marca=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=30)
    color=forms.CharField(max_length=15)
    anio=forms.IntegerField()
    precio=forms.IntegerField()

class SucursalesFormulario(forms.Form):
    ciudad=forms.CharField(max_length=35)
    pais=forms.CharField(max_length=15)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    admin_key = forms.CharField(
        max_length=50,
        required=False,
        label="admin key (if you have one)",
        widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'admin_key',
        ]
def clean_admin_key(self):
    key = self.cleaned_data.get("admin_key")
    if key and key != "Coderhouse":
        raise forms.ValidationError("La clave de administrador es incorrecta.")
    return key
