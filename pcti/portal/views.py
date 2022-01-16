from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Relatorios
from .models import Respostas
from .forms import RelatorioForm, RespostaForm
from django.contrib import messages
import datetime


# Create your views here.
@login_required
def variaveis_list(request, id):
    search = request.GET.get('search')
    if search:
        variaveis = Respostas.objects.filter(id_variavel__nome__icontains=search)
    else:
        variaveis = Respostas.objects.all().filter(id_relatorio_id=id)
    return render(request, 'portal/variaveis.html', {'variaveis': variaveis})


@login_required
def respostas_view(request, id):
    respostas = get_object_or_404(Respostas, pk=id)
    return render(request, 'portal/respostas.html', {'respostas': respostas})


@login_required
def relatorios_read(request):
    search = request.GET.get('search')
    if search:
        relatorios = Relatorios.objects.filter(id_dimensao__nome__icontains=search, user=request.user)
    else:
        relatorios_list = Relatorios.objects.all().order_by('-id_ano').filter(user=request.user)
        paginator = Paginator(relatorios_list, 3)
        page = request.GET.get('page')
        relatorios = paginator.get_page(page)
    return render(request, 'portal/home.html', {'relatorios': relatorios})


@login_required
def relatorio_create(request):
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            relatorio = form.save(commit=False)
            relatorio._delete = False
            relatorio.user = request.user
            relatorio.save()
            messages.info(request, 'Relatótio criado com sucesso.')
            return redirect('/')
    else:
        form = RelatorioForm()
        return render(request, 'create/relatoriocreate.html', {'form': form})


@login_required
def resposta_create(request):
    if request.method == 'POST':
        form = RespostaForm(request.POST)
        if form.is_valid():
            resposta = form.save(commit=False)
            resposta._delete = False
            resposta.save()
            messages.info(request, 'Resposta cadastrada com sucesso.')
            return redirect('/variaveis/')
    else:
        form = RespostaForm()
        return render(request, 'create/respostacreate.html', {'form': form})


@login_required
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


@login_required
def resposta_update(request, id):
    resposta = get_object_or_404(Respostas, pk=id)
    form = RespostaForm(instance=resposta)
    if request.method == 'POST':
        form = RespostaForm(request.POST, instance=resposta)
        if form.is_valid():
            resposta.save()
            messages.info(request, 'Resposta alterada com sucesso.')
            return redirect('/variaveis/')
        else:
            return render(request, 'update/respostaupdate.html', {'form': form, 'resposta': resposta})
    else:
        return render(request, 'update/respostaupdate.html', {'form': form, 'resposta': resposta})


@login_required
def relatorio_delete(request, id):
    relatorio = get_object_or_404(Relatorios, pk=id)
    relatorio.delete()
    messages.info(request, 'Dados deletados com sucesso.')
    return redirect('/')


@login_required
def resposta_delete(request, id):
    resposta = get_object_or_404(Respostas, pk=id)
    resposta.delete()
    messages.info(request, 'Dados deletados com sucesso.')
    return redirect('/variaveis/')


def dashboard(request):
    today = datetime.date.today()
    last_year = today.year - 1
    curremtIncome = get_object_or_404(Respostas, id_variavel__descricao__icontains='Receita', id_ano_base__ano=2017)
    return render(request, 'portal/dashboard.html', {'curremtIncome': curremtIncome, 'last_year': last_year})
