from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCriate, UsuarioUpdate

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCriate.as_view(), name='registrar'),
    path('atualizar-dados/', UsuarioUpdate.as_view(), name='atualizar-dados'),
]
