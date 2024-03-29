from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import DespesaForm
from .models import Despesa

from weasyprint import HTML


@login_required()
def listar_despesas(request):
    template_name = 'despesas/listar_despesas.html'
    despesas = Despesa.objects.all()
    total_despesas = Despesa.objects.all().aggregate(Sum('des_valordespesa'))
    media_despesas = Despesa.objects.all().aggregate(Avg('des_valordespesa'))

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Retorna a consulta se apenas a data inicial estiver preenchida
    if start_date and not end_date:
        despesas = despesas.filter(des_datadespesa=start_date)
        total_despesas = Despesa.objects.filter(des_datadespesa=start_date).aggregate(Sum('des_valordespesa'))
        media_despesas = Despesa.objects.filter(des_datadespesa=start_date).aggregate(Avg('des_valordespesa'))
    # Retorna a consulta se apenas a data inicial estiver preenchida
    elif not start_date and end_date:
        despesas = despesas.filter(des_datadespesa=end_date)
        total_despesas = Despesa.objects.filter(des_datadespesa=end_date).aggregate(Sum('des_valordespesa'))
        media_despesas = Despesa.objects.filter(des_datadespesa=end_date).aggregate(Avg('des_valordespesa'))
    # Retorna a consulta de ambas as datas estarem preenchidas
    if start_date and end_date:
        # o parse Converte em data e adiciona um dia.
        end_date = parse(end_date)
        despesas = despesas.filter(des_datadespesa__range=[start_date, end_date])
        total_despesas = Despesa.objects.filter(des_datadespesa__range=[start_date, end_date]).aggregate(
            Sum('des_valordespesa'))
        media_despesas = Despesa.objects.filter(des_datadespesa__range=[start_date, end_date]).aggregate(
            Avg('des_valordespesa'))

    context = {
        'despesas': despesas,
        'total_despesas': total_despesas,
        'media_despesas': media_despesas,
    }
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
    context = {
        'form': form,
    }
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


@login_required
def rel_despesas(request):
    template_name = 'despesas/rel_despesas.html'
    despesas = Despesa.objects.all().order_by('des_datadespesa')
    context = {'despesas': despesas}

    # Renderizado
    html_string = render_to_string(template_name, context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/rel_despesas.pdf')

    fs = FileSystemStorage('/tmp')

    with fs.open('rel_despesas.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        # Faz o download do arquivo PDF
        # response['Content-Disposition'] = 'attachment; filename="rel_despesas.pdf"'

        # Abre o PDF direto no navegador
        response['Content-Disposition'] = 'attachment; filename="rel_despesas.pdf"'
    return response

# @login_required()
# def consultar_despesas(request):
#     template_name = 'despesas/consultar_despesas.html'
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')
#
#     '''Retorna o range de datas escolhido para a consulta'''  # 3 e 4
#     if start_date and end_date:
#         form = form.filter(data__range=[start_date, end_date])
