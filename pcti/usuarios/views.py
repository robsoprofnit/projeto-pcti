from django.views.generic.edit import CreateView, UpdateView
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from cadastros.models import Pessoa


# Create your views here.


class UsuarioCriate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='GestorCTIC')
        form.instance.desativar = 0

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Pessoa.objects.create(id_user=self.object)

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Registro de novo usuário"

        return context


class UsuarioUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Pessoa
    fields = ['nome', 'cpf', 'nome_social']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):

        self.object = get_object_or_404(Pessoa, id_user=self.request.user)

        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(self, **kwargs)

        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"

        return context
