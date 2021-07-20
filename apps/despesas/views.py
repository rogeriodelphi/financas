from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DespesaForm
from .models import Despesa


@login_required()
def listar_despesas(request):
    template_name = 'despesas/listar_despesas.html'
    despesas = Despesa.objects.all()
    context = {'despesas': despesas}
    return render(request, template_name, context)


@login_required()
def inserir_despesa(request):
    template_name = 'despesas/inserir_despesa.html'
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('despesas:listar_despesas')
    form = DespesaForm()
    context = {'form': form}
    return render(request, template_name, context)

@login_required()
def listar_detalhe_despesa(request, id):
    template_name = 'despesas/listar_detalhe_despesa.html'
    despesa = Despesa.objects.get(id=id)
    context = {'despesa': despesa}
    return render(request, template_name, context)


@login_required()
def editar_despesa(request, id):
    template_name = 'despesas/editar_despesa.html'
    despesa = Despesa.objects.get(id=id)
    form = DespesaForm(request.POST or None, instance=despesa)
    if form.is_valid():
        form.save()
        return redirect('despesas:listar_despesas')
    context = {'form': form}
    return render(request, template_name, context)


@login_required()
def excluir_despesa(request, id):
    template_name = 'despesas/excluir_despesa.html'
    form = Despesa.objects.get(id=id)
    context = {'form': form}
    if request.method == 'POST':
        form.delete()
        return redirect('despesas:listar_despesas')
    return render(request, template_name, context)


# @login_required()
# def consultar_despesas(request):
#     template_name = 'despesas/consultar_despesas.html'

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    '''Retorna o range de datas escolhido para a consulta'''  # 3 e 4
    if start_date and end_date:
        form = form.filter(data__range=[start_date, end_date])
