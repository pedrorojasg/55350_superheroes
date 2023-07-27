from django import forms


class HeroeFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    nombre_real = forms.CharField(required=False, max_length=64)
    residencia = forms.CharField(required=True, max_length=64)
