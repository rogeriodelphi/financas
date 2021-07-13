from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.fornecedores.forms import FornecedorForm
from apps.fornecedores.models import Fornecedor


@login_required()
def listar_fornecedores(request):
    template_name = 'fornecedores/listar_fornecedores.html'
    fornecedores = Fornecedor.objects.all()
    context = {'fornecedores': fornecedores}
    return render(request, template_name, context)


@login_required()
def inserir_fornecedor(request):
    template_name = 'fornecedores/inserir_fornecedor.html'
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('fornecedores:listar_fornecedores')
    form = FornecedorForm()
    context = {'form': form}
    return render(request, template_name, context)


@login_required()
def listar_detalhe_fornecedor(request, id):
    template_name = 'fornecedores/listar_detalhe_fornecedor.html'
    fornecedor = Fornecedor.objects.get(id=id)
    context = {'fornecedor': fornecedor}
    return render(request, template_name, context)


@login_required()
def editar_fornecedor(request, id):
    template_name = 'fornecedores/editar_fornecedor.html'
    fornecedor = Fornecedor.objects.get(id=id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    if form.is_valid():
        form.save()
        return redirect('fornecedores:listar_fornecedores')
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def excluir_fornecedor(request, id):
    template_name = 'fornecedores/excluir_fornecedor.html'
    form = Fornecedor.objects.get(id=id)
    context = {'form': form}
    if request.method == "POST":
        form.delete()
        return redirect('fornecedores:listar_fornecedores')
    return render(request, template_name, context)
