from django import forms
from django.forms import fields

from aplicacao.models import Formulario

class MeuFormulario(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'
    