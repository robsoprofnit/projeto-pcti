from django.urls import path
# from . import views
from .views import AnoBaseCreate, RegiaoCreate, RelatorioCreate
from .views import AnoBaseUpdate, RegiaoUpdate, RelatorioUpdate
from .views import AnoBaseDelete, RegiaoDelete, RelatorioDelete
from .views import AnoBaseList, RegiaoList, RelatorioList

urlpatterns = [
    path('cadastrar/ano/', AnoBaseCreate.as_view(), name='cadastar-ano'),
    path('cadastrar/regiao/', RegiaoCreate.as_view(), name='cadastrar-regiao'),
    path('cadastrar/relatorio/', RelatorioCreate.as_view(), name='cadastrar-relatorio'),
    # path('', views.relatorios_read, name='index'),
    # path('variaveis/<int:id>', views.variaveis_list, name='variaveis-view'),
    # path('variaveis/respostas/<int:id>', views.respostas_view, name='respostas-view'),
    # path('create/', views.relatorio_create, name='relatorio-create'),
    # path('update/<int:id>', views.relatorio_update, name='relatorio-update'),
    # path('delete/<int:id>', views.relatorio_delete, name='relatorio-delete'),
    # path('dashboard/', views.dashboard, name='dashboard-view'),
    # path('variaveis/create/', views.resposta_create, name='resposta-create'),
    # path('variaveis/update/<int:id>', views.resposta_update, name='resposta-update'),
    # path('variaveis/delete/<int:id>', views.resposta_delete, name='resposta-delete'),

    path('editar/ano/<int:pk>', AnoBaseUpdate.as_view(), name='editar-ano'),
    path('editar/regiao/<int:pk>', RegiaoUpdate.as_view(), name='editar-regiao'),
    path('editar/relatorio/<int:pk>', RelatorioUpdate.as_view(), name='editar-relatorio'),

    path('excluir/ano/<int:pk>', AnoBaseDelete.as_view(), name='excluir-ano'),
    path('excluir/regiao/<int:pk>', RegiaoDelete.as_view(), name='excluir-regiao'),
    path('excluir/relatorio/<int:pk>', RelatorioDelete.as_view(), name='excluir-relatorio'),

    path('listar/ano/', AnoBaseList.as_view(), name='listar-ano'),
    path('listar/regiao/', RegiaoList.as_view(), name='listar-regiao'),
    path('listar/relatorio/', RelatorioList.as_view(), name='listar-relatorio'),
]
