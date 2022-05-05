from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404


# Create your views here.



class UsuarioCriate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='GestorCTIC')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        from pcti.cadastros.models import User_pessoa
        User_pessoa.objects.create(id_user=self.object)

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Registro de novo usuário"

        return context