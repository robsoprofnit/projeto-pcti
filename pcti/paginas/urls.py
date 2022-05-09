from django.urls import path
from .views import PaginaInicial, SobreView, DashboardView, ConfiguracoesView


urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('configuracoes/', ConfiguracoesView.as_view(), name='configuracoes'),
]
