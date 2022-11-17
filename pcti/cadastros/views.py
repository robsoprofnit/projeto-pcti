from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from .decorator import group_required
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.db.models.aggregates import Avg
from .forms import RepostaForm
from django.contrib import messages
from django.shortcuts import redirect

import csv
from django.http import HttpResponse


# Create your views here.

class RepostaView(CreateView):
    model = Respostas
    fields = ['id_ano_base', 'id_pessoa_juridica', 'id_dimensao', 'id_subindicador',
              'id_variavel', 'id_relatorio', 'resposta', 'tag']
    template_name = 'cadastros/indicadores/form-resposta-update.html'
    success_url = reverse_lazy('listar-relatorio')

    def form_valid(self, form):
        form.instance.id_user = self.request.user
        form.instance.desativar = 0

        valor = super().form_valid(form)

        return valor


def drop_list(request):
    dimensao = Dimensoes.objects.all()
    variavel = Variavel.objects.all()

    return render(request, 'cadastros/indicadores/form-resposta-update.html',
                  {"Dimensao": dimensao, "Variavel": variavel})


###################### CREATE VIEWS ######################


class AnoBaseCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Ano_base
    fields = ['ano', 'desativar']
    template_name = 'cadastros/form.html'
    # success_url = reverse_lazy('listar-ano')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item cadastrado com sucesso")
        return reverse('listar-ano')

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
    # success_url = reverse_lazy('listar-regiao')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item cadastrado com sucesso")
        return reverse('listar-regiao')


class RelatorioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador', u'GestorCTIC']
    model = Relatorios
    fields = ['id_pessoa_juridica', 'id_ano', 'id_dimensao']
    template_name = 'cadastros/form.html'
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item cadastrado com sucesso")
        return reverse('listar-relatorio2')

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
    # success_url = reverse_lazy('listar-variavel')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item cadastrado com sucesso")
        return reverse('variavel-create')


@login_required
@group_required(u'Administrador', u'GestorCTIC')
def resposta_create(request):
    dimensao = request.GET.get('dimensao')
    variaveis = Variavel.objects.filter(id_dimensao=dimensao)
    relatorios = Relatorios.objects.filter(id_dimensao_id=dimensao)
    context = {
        "variaveis": variaveis,
        "relatorios": relatorios,
        "teste": "121"
    }
    if request.method == 'POST':
        relatorio = None
        for chave, valor in request.POST.items():
            posicao = chave.split("-")
            if len(posicao) == 1 and chave == 'relatorio':
                relatorio = Relatorios.objects.get(pk=valor)
            elif chave != 'csrfmiddlewaretoken':
                id_variavel = posicao[1]
                variavel = Variavel.objects.get(pk=id_variavel)
                Respostas.objects.create(resposta=valor,
                                         id_variavel=variavel,
                                         id_relatorio=relatorio,
                                         id_user_id=request.user.pk,
                                         id_dimensao_id=dimensao,
                                         id_pessoa_juridica=relatorio.id_pessoa_juridica,
                                         id_ano_base=relatorio.id_ano,
                                         id_indicador=variavel.id_indicador)

    return render(request, "cadastros/indicadores/form-resposta.html", context=context)


class RespostaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador', u'GestorCTIC']
    form_class = RepostaForm
    template_name = 'cadastros/indicadores/form-resposta.html'
    # success_url = reverse_lazy('listar-relatorio')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item cadastrado com sucesso")
        return reverse('listar-relatorio')

    def get_form_kwargs(self):
        kwargs = super(RespostaCreate, self).get_form_kwargs()
        kwargs['dimensao'] = self.request.GET.get('dimensao')
        return kwargs

    def form_valid(self, form):
        form.instance.id_user = self.request.user
        form.instance.desativar = 0
        form.instance.id_pessoa_juridica_id = 1
        form.instance.id_dimensao_id = 1
        form.instance.id_indicador_id = 1
        form.instance.id_ano_base_id = 1

        valor = super().form_valid(form)

        return valor


class InstituicaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pessoa_juridica
    fields = ['nome', 'cnpj', 'razao_social', 'email', 'id_municipio', 'id_tipo_esfera']
    template_name = 'cadastros/form.html'
    # success_url = reverse_lazy('listar-instituicao')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item cadastrado com sucesso")
        return reverse('listar-instituicao')


class ResponsavelCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Responsavel_instituicao
    fields = ['id_pessoa', 'id_pessoa_juridica']
    template_name = 'cadastros/form.html'
    # success_url = reverse_lazy('Listar-responsavel')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item cadastrado com sucesso")
        return reverse('listar-responsavel')


###################### UPDATE VIEWS ######################


class AnoBaseUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Ano_base
    fields = ['ano']
    template_name = 'cadastros/form.html'
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item atualizado com sucesso")
        return reverse('listar-ano')

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


@login_required
@group_required(u'Administrador', u'GestorCTIC')
def resposta_update(request):
    dimensao = request.GET.get('dimensao')
    ano = request.GET.get('ano')
    instituicao = request.GET.get('instituicao')
    variaveis = Variavel.objects.filter(id_dimensao=dimensao)
    respostas = Respostas.objects.filter(id_dimensao_id=dimensao, id_ano_base_id=ano, id_pessoa_juridica_id=instituicao)
    context = {
        "variaveis": variaveis,
        "respostas": respostas,
        "relatorio": respostas[0].id_relatorio,
        "mensagem": ""
    }
    if request.method == 'POST':
        for chave, valor in request.POST.items():
            posicao = chave.split("-")
            if len(posicao) > 1:
                id_resposta = posicao[1]
                Respostas.objects.filter(pk=id_resposta).update(
                    resposta=valor
                )
                context["mensagem"] = "Item atualizado com sucesso"

    return render(request, "cadastros/indicadores/form-resposta-update.html", context=context)


class RespostaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Respostas
    fields = ['id_ano_base', 'id_pessoa_juridica', 'id_dimensao', 'id_subindicador',
              'id_variavel', 'id_relatorio', 'resposta', 'tag']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-relatorio')


class InstituicaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pessoa_juridica
    fields = ['nome', 'cnpj', 'razao_social', 'email', 'id_municipio', 'id_tipo_esfera']
    template_name = 'cadastros/form.html'
    # success_url = reverse_lazy('listar-instituicao')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item atualizado com sucesso")
        return reverse('listar-instituicao')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastrar Instituição'
        context['botao'] = 'Salvar'

        return context


class ResponsavelUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Responsavel_instituicao
    fields = ['id_pessoa', 'id_pessoa_juridica']
    template_name = 'cadastros/form.html'
    # success_url = reverse_lazy('listar-responsavel')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item atualizado com sucesso")
        return reverse('listar-responsavel')


###################### DELETE VIEWS ######################


class AnoBaseDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Administrador']
    model = Ano_base
    template_name = 'cadastros/form-delete.html'
    # success_url = reverse_lazy('listar-ano')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item deletado com sucesso")
        return reverse('listar-ano')


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
    # success_url = reverse_lazy('listar-relatorio2')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item deletado com sucesso")
        return reverse('listar-relatorio2')

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
    success_url = reverse_lazy('listar-relatorio')


class InstituicaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Pessoa_juridica
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-instituicao')
    # def get_success_url(self):
    #     return reverse('listar-instituicao')
    def post(self, request, *args, **kwargs):
            print("cheguei aqui####################################################")
            self.object = self.get_object()
            success_url = self.get_success_url()
            try:
                self.object.delete()
                messages.add_message(self.request, messages.INFO, "Item deletado com sucesso")
            except models.ProtectedError:
                messages.add_message(self.request, messages.WARNING, "Falha ao deletar. Item já está sendo utilizado")
            return redirect(success_url)


class ResponsavelDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Responsavel_instituicao
    template_name = 'cadastros/form-delete.html'
    # success_url = reverse_lazy('listar-responsavel')
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Item deletado com sucesso")
        return reverse('listar-responsavel')


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


class RelatorioList2(ListView):
    model = Relatorios
    template_name = 'cadastros/listas/relatorios.html'


class RelatorioList(ListView):
    model = Relatorios
    template_name = 'cadastros/listas/dimensoes.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RelatorioList, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        self.object_list = Relatorios.objects.filter(id_user=self.request.user)
        return self.object_list


class VariavelList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Variavel
    template_name = 'cadastros/listas/variaveis.html'


class RespostaList(ListView):
    model = Respostas
    template_name = 'cadastros/listas/respostas.html'

    def get_queryset(self):
        filtro = self.kwargs['pk']
        self.object_list = Respostas.objects.filter(id_relatorio=filtro)
        return self.object_list

    def Somar(self):
        self.soma = Respostas.objects.all().aggregate(total=Avg(Respostas.resposta))
        return self.soma


class InstituicaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pessoa_juridica
    template_name = 'cadastros/listas/instituicao.html'


class ResponsavelList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Responsavel_instituicao
    template_name = 'cadastros/listas/responsavel.html'


# Generate Text File List
def export_to_csv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="picti_data.csv"'},
    )

    # Create a csv writer
    writer = csv.writer(response, delimiter=';')

    # Designate the model
    respostas = Respostas.objects.all()

    # Add columns headings to the csv file
    writer.writerow(['id_ano_base', 'id_pessoa_juridica', 'id_dimensao', 'id_indicador', 'id_variavel', 'id_relatorio',
                     'resposta'])

    # Loop through and output
    for resposta in respostas:
        writer.writerow([resposta.id_ano_base, resposta.id_pessoa_juridica, resposta.id_dimensao, resposta.id_indicador,
                         resposta.id_variavel, resposta.id_relatorio, resposta.resposta])

    return response