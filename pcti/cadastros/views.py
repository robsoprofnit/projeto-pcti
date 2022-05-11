from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404, render
from .forms import RepostaForm

import json


# Create your views here.

###################### CREATE VIEWS ######################


class AnoBaseCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Ano_base
    fields = ['ano', 'desativar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ano')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Ano Base'

        return context


class RegiaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Regiao
    fields = ['nome', 'desativar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-regiao')


class RelatorioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador', u'GestorCTIC']
    model = Relatorios
    fields = ['id_pessoa_juridica', 'id_ano', 'id_dimensao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-relatorio')

    def form_valid(self, form):

        form.instance.id_user = self.request.user
        form.instance.desativar = 0

        valor = super().form_valid(form)

        return valor


class VariavelCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador', u'GestorCTIC']
    model = Variavel
    fields = ['nome', 'descricao', 'tag', 'id_dimensao', 'desativar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-variavel')


class RespostaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador', u'GestorCTIC']
    model = Respostas
    fields = ['resposta', 'tag', 'id_ano_base', 'id_pessoa_juridica',
              'id_dimensao', 'id_variavel', 'id_relatorio']
    template_name = 'cadastros/resposta-form.html'
    success_url = reverse_lazy('listar-resposta')


    def form_valid(self, form):

        form.instance.id_user = self.request.user
        form.instance.desativar = 0

        valor = super().form_valid(form)

        return valor

def respostaform_page(request):
    context = {}
    respostaform = RepostaForm
    context['respostaform'] = respostaform

    dimensao = DimensaoList
    varialvel = VariavelList

    json_dimensao = json.dumps(dimensao)
    json_variavel = json.dumps(varialvel)

    context['json_dimensao'] = json_dimensao
    context['json_variavel'] = json_variavel

    return render(request, 'cadastros/resposta-form.html', context)


###################### UPDATE VIEWS ######################


class AnoBaseUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Ano_base
    fields = ['ano', 'desativar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ano')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Ano Base'
        context['botao'] = 'Salvar'

        return context


class RegiaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Regiao
    fields = ['nome', 'desativar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-regiao')


class RelatorioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Relatorios
    fields = ['id_pessoa_juridica', 'id_ano', 'id_dimensao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-relatorio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Relatorios, pk=self.kwargs['pk'], id_user=self.request.user)
        return self.object

    def form_valid(self, form):

        form.instance.id_user = self.request.user

        valor = super().form_valid(form)

        return valor


class VariavelUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Variavel
    fields = ['nome', 'descricao', 'tag', 'id_dimensao', 'desativar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-variavel')


class RespostaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Respostas
    fields = ['resposta', 'tag', 'id_ano_base', 'id_instituicao',
              'id_respondido_por', 'id_variavel', 'id_relatorio', 'desativar']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-resposta')


###################### DELETE VIEWS ######################


class AnoBaseDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Ano_base
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-ano')


class RegiaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Regiao
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-regiao')


class RelatorioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Relatorios
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-relatorio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Relatorios, pk=self.kwargs['pk'], id_user=self.request.user)
        return self.object


class VariavelDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Variavel
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-variavel')


class RespostaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Respostas
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-resposta')


###################### LISTA ######################


class AnoBaseList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Ano_base
    template_name = 'cadastros/listas/ano.html'


class RegiaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Regiao
    template_name = 'cadastros/listas/regiao.html'


class DimensaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Dimensoes
    template_name = 'cadastros/listas/dimensao.html'


class RelatorioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Relatorios
    template_name = 'cadastros/listas/relatorios.html'

    def get_queryset(self):
        self.object_list = Relatorios.objects.filter(id_user=self.request.user)
        return self.object_list

class VariavelList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Variavel
    template_name = 'cadastros/listas/variaveis.html'


class RespostaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Respostas
    template_name = 'cadastros/listas/respostas.html'

    def get_queryset(self):
        filtro = self.kwargs['pk']
        self.object_list = Respostas.objects.filter(id_relatorio=filtro)
        return self.object_list
