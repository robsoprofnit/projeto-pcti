from django import forms
from django.contrib import admin
from .models import Respostas


class RepostaForm(forms.ModelForm):
    class Meta:
        model = Respostas
        fields = ['id_ano_base', 'id_variavel', 'resposta']
