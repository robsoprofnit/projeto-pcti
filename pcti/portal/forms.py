from django import forms
from .models import *


class RelatorioForm(forms.ModelForm):

    class Meta:
        model = Relatorios
        fields = ('id_ano',
                  'id_instituicao',
                  'id_dimensao',)


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Respostas
        fields = ('resposta',
                  'tag',
                  'id_ano_base',
                  'id_instituicao',
                  'id_variavel',
                  'id_relatorio',
                  'id_respondido_por',)
