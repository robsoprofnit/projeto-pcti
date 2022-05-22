from django import forms
from .models import Respostas


class RepostaForm(forms.ModelForm):
    class Meta:
        model = Respostas
        fields = ['id_variavel', 'resposta']

