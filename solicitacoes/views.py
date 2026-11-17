from django.shortcuts import render, redirect
from .models import Solicitacao
from .forms import SolicitacaoForm


def listar_solicitacoes(request):
    solicitacoes = Solicitacao.objects.select_related('cliente').all()

    return render(request, 'solicitacoes/listar.html', {
        'solicitacoes': solicitacoes
    })


def cadastrar_solicitacao(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_solicitacoes')
    else:
        form = SolicitacaoForm()

    return render(request, 'solicitacoes/cadastrar.html', {
        'form': form
    })