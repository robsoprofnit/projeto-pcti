from django.urls import path
from . import views

urlpatterns = [
    path('', views.relatorios_read, name='index'),
    path('variaveis/<int:id>', views.variaveis_list, name='variaveis-view'),
    path('variaveis/respostas/<int:id>', views.respostas_view, name='respostas-view'),
    path('create/', views.relatorio_create, name='relatorio-create'),
    path('update/<int:id>', views.relatorio_update, name='relatorio-update'),
    path('delete/<int:id>', views.relatorio_delete, name='relatorio-delete'),
    path('dashboard/', views.dashboard, name='dashboard-view'),
    path('variaveis/create/', views.resposta_create, name='resposta-create'),
    path('variaveis/update/<int:id>', views.resposta_update, name='resposta-update'),
    path('variaveis/delete/<int:id>', views.resposta_delete, name='resposta-delete'),
]
