from django.urls import path
from .views import ManagerView, SobreView, dashboard, ConfiguracoesView, ModeloAdmView, InitialView


urlpatterns = [
    path('', InitialView.as_view(), name='inicio'),
    path('manager/', ManagerView.as_view(), name='manager'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('dashboard/', dashboard, name='dashboard'),
    path('configuracoes/', ConfiguracoesView.as_view(), name='configuracoes'),
    path('modeloadm/', ModeloAdmView.as_view(), name='modelo-adm'),
]
