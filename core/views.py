from operator import index

from django.urls import reverse_lazy
from .models import AtividadeModel
from .forms import AtividadeModelForm
from django.shortcuts import redirect, render, HttpResponse
import datetime

data = datetime.date.today()


def Cadastrar(request):
    if request.method == 'POST':
        form = AtividadeModelForm(request.POST)
        if form.is_valid():
            titulo = form.data['titulo']
            data = form.data['data']
            local = form.data['local']
            tarefa = form.data['tarefa']

            form.save()

        return redirect('index')

    else:
        form = AtividadeModelForm
        return render(request, 'create.html', {'form': form})


def Atualizar(request, id):
    tarefa = AtividadeModel.objects.get(pk=id)
    return render(request, 'update.html', {'form': tarefa})


def ConfirmarAtt(request):
    
    if request.method == 'POST':
        form = AtividadeModelForm(request.POST)

        if form.is_valid():

            task = AtividadeModel()
            task.id = form.data['id']
            task.titulo = form.data['titulo']
            task.data = form.data['data']
            task.local = form.data['local']
            task.tarefa = form.data['tarefa']

            task.save()

            form = AtividadeModelForm
            return redirect('index')


def Deletar(request, id):
    tarefa = AtividadeModel.objects.get(pk=id)

    if tarefa != None:
        tarefa.delete()
    return redirect('index')


def Index(request):

    atividades = []
    context = {'listaAtividades': atividades}
    atividades = AtividadeModel.objects.all()

    for atividade in atividades:
        if atividade.data == data:
            context['listaAtividades'].append(atividade)

    return render(request, 'index.html', context)
