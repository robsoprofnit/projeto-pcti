from django import forms
from .models import Respostas, Variavel


class RepostaForm(forms.ModelForm):
    class Meta:
        model = Respostas
        fields = ['id_ano_base', 'id_variavel', 'resposta']

    def __init__(self, *args, **kwargs):
        dimensao = kwargs.pop("dimensao")
        super(RepostaForm, self).__init__(*args, **kwargs)
        self.fields["id_variavel"].queryset = Variavel.objects.filter(id_dimensao=dimensao)
