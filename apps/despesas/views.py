from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Despesa
from .forms import DespesaForm

@login_required()
def listar_despesas(request):
    template_name = 'despesas/listar_despesas.html'
    despesas = Despesa.objects.all()
    context = {'despesas': despesas}
    return render(request, template_name, context)

@login_required()
def inserir_despesa(request):
    template_name = 'despesas/inserir_despesas.html'
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('despesas:listar_despesas')
    form = DespesaForm()
    context = {'form': form}
    return render(request, template_name, context)