from tkinter import E
from django.views.generic import TemplateView, ListView
from .service import generate_dashboard_info
from cadastros.models import Respostas
from django.shortcuts import render

from cadastros.models import (
    Respostas,
    Ano_base,
    Uf,
    Dimensoes,
    Indicadores,
    Pessoa_juridica,
)
from django.db.models import Sum

# Create your views here.


class ManagerView(TemplateView):
    template_name = "paginas/index-manager.html"


class InitialView(TemplateView):
    template_name = "paginas/dashboard.html"


class SobreView(TemplateView):
    template_name = "paginas/sobre.html"


# class DashboardView(ListView):
#     model = Respostas
#     template_name = 'paginas/dashboard.html'


def dashboard(request):
    context = {}
    ano = Ano_base.objects.first()
    instituicao = Pessoa_juridica.objects.get(id=1)
    if request.method == "POST":
        ano_id = request.POST.get("ano")
        instituicao_id = request.POST.get("instituicao")
        if ano and instituicao:
            ano = Ano_base.objects.get(pk=ano_id)
            instituicao = Pessoa_juridica.objects.get(pk=instituicao_id)
            context = generate_dashboard_info(ano, instituicao)
            context["ano_selecionado"] = ano
            context["instituicao_selecionada"] = instituicao
    else:
        context = generate_dashboard_info(ano, instituicao)
        context["ano_selecionado"] = ano
        context["instituicao_selecionada"] = instituicao
    context["filtro_anos"] = Ano_base.objects.all()
    context["filtro_instituicoes"] = Pessoa_juridica.objects.all()
    return render(request, "paginas/dashboard.html", context=context)


def teste():
    pass


class ConfiguracoesView(TemplateView):
    template_name = "paginas/configuracoes.html"


class ModeloAdmView(TemplateView):
    template_name = "paginas/modelo-admin.html"
