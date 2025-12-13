from django import forms

class AutosFormulario(forms.Form):
    marca=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=30)
    color=forms.CharField(max_length=15)
    anio=forms.IntegerField()
    precio=forms.IntegerField()