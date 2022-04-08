from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Relatorios, Ano_base, Regiao, Variavel
from .models import Respostas


# Create your views here.

###################### CREATE VIEWS ######################


class AnoBaseCreate(CreateView):
    model = Ano_base
    fields = ['ano', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ano')


class RegiaoCreate(CreateView):
    model = Regiao
    fields = ['nome', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-regiao')


class RelatorioCreate(CreateView):
    model = Relatorios
    fields = ['id_instituicao', 'id_ano', 'id_dimensao', 'user']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-relatorio')


class VariavelCreate(CreateView):
    model = Variavel
    fields = ['nome', 'descricao', 'tag', 'id_dimensao', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-variavel')


class RespostaCreate(CreateView):
    model = Respostas
    fields = ['resposta', 'tag', 'id_ano_base', 'id_instituicao',
              'id_respondido_por', 'id_variavel', 'id_relatorio', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-resposta')


###################### UPDATE VIEWS ######################


class AnoBaseUpdate(UpdateView):
    model = Ano_base
    fields = ['ano', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ano')


class RegiaoUpdate(UpdateView):
    model = Regiao
    fields = ['nome', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-regiao')


class RelatorioUpdate(UpdateView):
    model = Relatorios
    fields = ['id_instituicao', 'id_ano', 'id_dimensao', 'user']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-relatorio')


class VariavelUpdate(UpdateView):
    model = Variavel
    fields = ['nome', 'descricao', 'tag', 'id_dimensao', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-variavel')


class RespostaUpdate(UpdateView):
    model = Respostas
    fields = ['resposta', 'tag', 'id_ano_base', 'id_instituicao',
              'id_respondido_por', 'id_variavel', 'id_relatorio', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-resposta')


###################### DELETE VIEWS ######################


class AnoBaseDelete(DeleteView):
    model = Ano_base
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-ano')


class RegiaoDelete(DeleteView):
    model = Regiao
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-regiao')


class RelatorioDelete(DeleteView):
    model = Relatorios
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-relatorio')


class VariavelDelete(DeleteView):
    model = Variavel
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-variavel')


class RespostaDelete(DeleteView):
    model = Respostas
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-resposta')


###################### LISTA ######################


class AnoBaseList(ListView):
    model = Ano_base
    template_name = 'cadastros/listas/ano.html'


class RegiaoList(ListView):
    model = Regiao
    template_name = 'cadastros/listas/regiao.html'


class RelatorioList(ListView):
    model = Relatorios
    template_name = 'cadastros/listas/relatorios.html'


class VariavelList(ListView):
    model = Variavel
    template_name = 'cadastros/listas/variaveis.html'


class RespostaList(ListView):
    model = Respostas
    template_name = 'cadastros/listas/respostas.html'

