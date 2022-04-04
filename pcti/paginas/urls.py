from django.contrib import admin
from django.urls import path
from .views import PaginaInicial, SobreView, PaginaInicial2, DashboardView, RelatoriosView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaginaInicial.as_view(), name='inicio'),
    path('relatorios/', RelatoriosView.as_view(), name='relatorios'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('index2/', PaginaInicial2.as_view(), name='index2'),
]
