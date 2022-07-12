from django.urls import path
from .views import ManagerView, SobreView, DashboardView, ConfiguracoesView, ModeloAdmView, InitialView


urlpatterns = [
    path('', InitialView.as_view(), name='inicio'),
    path('manager/', ManagerView.as_view(), name='manager'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('dashboard/<int:year>/<str:name>', DashboardView.as_view(), name='dashboard'),
    path('configuracoes/', ConfiguracoesView.as_view(), name='configuracoes'),
    path('modeloadm/', ModeloAdmView.as_view(), name='modelo-adm'),
]
