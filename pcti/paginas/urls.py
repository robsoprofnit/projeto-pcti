from django.urls import path
from .views import PaginaInicial, SobreView, PaginaInicial2


urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('index2/', PaginaInicial2.as_view(), name='index2'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]
