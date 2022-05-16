from django.views.generic import TemplateView, ListView
from cadastros.models import Respostas
# Create your views here.


class PaginaInicial(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'sobre.html'


class DashboardView(ListView):
    model = Respostas
    template_name = 'dashboard.html'


class ConfiguracoesView(TemplateView):
    template_name = 'configuracoes.html'


class ModeloAdmView(TemplateView):
    template_name = 'modelo-admin.html'