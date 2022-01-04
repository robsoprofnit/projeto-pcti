from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Relatorios
from .models import Respostas
from .forms import RelatorioForm
from django.contrib import messages


# Create your views here.
def variaveis_list(request):
    variaveis = Respostas.objects.all()
    return render(request, 'portal/variaveis.html', {'variaveis': variaveis})


def respostas_view(request, id):
    respostas = get_object_or_404(Respostas, pk=id)
    return render(request, 'portal/respostas.html', {'respostas': respostas})


def relatorios_read(request):
    relatorios_list = Relatorios.objects.all().order_by('-id_ano')
    paginator = Paginator(relatorios_list, 3)
    page = request.GET.get('page')
    relatorios = paginator.get_page(page)
    return render(request, 'portal/home.html', {'relatorios': relatorios})


def relatorio_create(request):
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            relatorio = form.save(commit=False)
            relatorio._delete = False
            relatorio.save()
            messages.info(request, 'Relatótio criado com sucesso.')
            return redirect('/')
    else:
        form = RelatorioForm()
        return render(request, 'create/relatoriocreate.html', {'form': form})


def relatorio_update(request, id):
    relatorio = get_object_or_404(Relatorios, pk=id)
    form = RelatorioForm(instance=relatorio)
    if request.method == 'POST':
        form = RelatorioForm(request.POST, instance=relatorio)
        if form.is_valid():
            relatorio.save()
            messages.info(request, 'Relatótio alterado com sucesso.')
            return redirect('/')
        else:
            return render(request, 'update/relatorioupdate.html', {'form': form, 'relatorio': relatorio})
    else:
        return render(request, 'update/relatorioupdate.html', {'form': form, 'relatorio': relatorio})


def relatorio_delete(request, id):
    relatorio = get_object_or_404(Relatorios, pk=id)
    relatorio.delete()
    messages.info(request, 'Relatório deletado com sucesso.')
    return redirect('/')
