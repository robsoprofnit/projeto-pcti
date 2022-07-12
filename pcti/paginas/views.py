from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from cadastros.models import Respostas
from datetime import datetime
# Create your views here.


class ManagerView(TemplateView):
    template_name = 'paginas/index-manager.html'


class InitialView(TemplateView):
    template_name = 'paginas/dashboard.html'


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


class DashboardView(ListView):
    model = Respostas
    template_name = 'paginas/dashboard.html'

    def dashboard(request, year, institution):
        # Get current year
        year = 2021
        # Get institution
        institution = "setec"
        return render(request,
                      {
                          "year": year,
                          "institution": institution,
                      })


class ConfiguracoesView(TemplateView):
    template_name = 'paginas/configuracoes.html'


class ModeloAdmView(TemplateView):
    template_name = 'paginas/modelo-admin.html'