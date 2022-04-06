from django.views.generic import TemplateView
# Create your views here.


class PaginaInicial(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'sobre.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

