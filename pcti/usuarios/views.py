from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.urls import reverse_lazy

# Create your views here.


class UsuarioCriate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Registro de novo usuário"

        return context