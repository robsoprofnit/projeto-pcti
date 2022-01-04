from django import forms
from .models import *


class RelatorioForm(forms.ModelForm):

    class Meta:
        model = Relatorios
        fields = ('id_ano', 'id_instituicao', 'id_dimensao')