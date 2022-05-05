from django.urls import path
from .views import AnoBaseCreate, RegiaoCreate, RelatorioCreate, VariavelCreate, RespostaCreate
from .views import AnoBaseUpdate, RegiaoUpdate, RelatorioUpdate, VariavelUpdate, RespostaUpdate
from .views import AnoBaseDelete, RegiaoDelete, RelatorioDelete, VariavelDelete, RespostaDelete
from .views import AnoBaseList, RegiaoList, RelatorioList, VariavelList, RespostaList

urlpatterns = [
    path('cadastrar/ano/', AnoBaseCreate.as_view(), name='cadastrar-ano'),
    path('cadastrar/regiao/', RegiaoCreate.as_view(), name='cadastrar-regiao'),
    path('cadastrar/relatorio/', RelatorioCreate.as_view(), name='cadastrar-relatorio'),
    path('cadastrar/variavel/', VariavelCreate.as_view(), name='cadastrar-variavel'),
    path('cadastrar/resposta/', RespostaCreate.as_view(), name='cadastrar-resposta'),

    path('editar/ano/<int:pk>', AnoBaseUpdate.as_view(), name='editar-ano'),
    path('editar/regiao/<int:pk>', RegiaoUpdate.as_view(), name='editar-regiao'),
    path('editar/relatorio/<int:pk>', RelatorioUpdate.as_view(), name='editar-relatorio'),
    path('editar/variavel/<int:pk>', VariavelUpdate.as_view(), name='editar-variavel'),
    path('editar/resposta/<int:pk>', RespostaUpdate.as_view(), name='editar-resposta'),

    path('excluir/ano/<int:pk>', AnoBaseDelete.as_view(), name='excluir-ano'),
    path('excluir/regiao/<int:pk>', RegiaoDelete.as_view(), name='excluir-regiao'),
    path('excluir/relatorio/<int:pk>', RelatorioDelete.as_view(), name='excluir-relatorio'),
    path('excluir/variavel/<int:pk>', VariavelDelete.as_view(), name='excluir-variavel'),
    path('excluir/resposta/<int:pk>', RespostaDelete.as_view(), name='excluir-resposta'),

    path('listar/ano/', AnoBaseList.as_view(), name='listar-ano'),
    path('listar/regiao/', RegiaoList.as_view(), name='listar-regiao'),
    path('listar/relatorio/', RelatorioList.as_view(), name='listar-relatorio'),
    path('listar/variavel/', VariavelList.as_view(), name='listar-variavel'),
    path('listar/resposta/<int:pk>', RespostaList.as_view(), name='listar-resposta'),
]
