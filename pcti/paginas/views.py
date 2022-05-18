from django.views.generic import TemplateView, ListView
from cadastros.models import Respostas
# Create your views here.


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


class DashboardView(ListView):
    model = Respostas
    template_name = 'paginas/dashboard.html'


class ConfiguracoesView(TemplateView):
    template_name = 'paginas/configuracoes.html'


class ModeloAdmView(TemplateView):
    template_name = 'paginas/modelo-admin.html'