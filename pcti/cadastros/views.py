from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Relatorios, Ano_base, Regiao, Variavel
from .models import Respostas
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.

###################### CREATE VIEWS ######################


class AnoBaseCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Ano_base
    fields = ['ano', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ano')


class RegiaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Regiao
    fields = ['nome', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-regiao')


class RelatorioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador', u'GestorCTIC']
    model = Relatorios
    fields = ['id_instituicao', 'id_ano', 'id_dimensao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-relatorio')

    def form_valid(self, form):

        form.instance.user = self.request.user
        form.instance._delete = 0

        url = super().form_valid(form)

        return url


class VariavelCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador', u'GestorCTIC']
    model = Variavel
    fields = ['nome', 'descricao', 'tag', 'id_dimensao', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-variavel')


class RespostaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador', u'GestorCTIC']
    model = Respostas
    fields = ['resposta', 'tag', 'id_ano_base', 'id_instituicao',
              'id_respondido_por', 'id_variavel', 'id_relatorio', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-resposta')


###################### UPDATE VIEWS ######################


class AnoBaseUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Ano_base
    fields = ['ano', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ano')


class RegiaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Regiao
    fields = ['nome', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-regiao')


class RelatorioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Relatorios
    fields = ['id_instituicao', 'id_ano', 'id_dimensao', 'user']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-relatorio')


class VariavelUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Variavel
    fields = ['nome', 'descricao', 'tag', 'id_dimensao', '_delete']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-variavel')


class RespostaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Respostas
    fields = ['resposta', 'tag', 'id_ano_base', 'id_instituicao',
              'id_respondido_por', 'id_variavel', 'id_relatorio', '_delete']
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


class RelatorioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Relatorios
    template_name = 'cadastros/listas/relatorios.html'



class VariavelList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Variavel
    template_name = 'cadastros/listas/variaveis.html'


class RespostaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Respostas
    template_name = 'cadastros/listas/respostas.html'

