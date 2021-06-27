from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from nat_despesas.forms import NatDespesaForm
from nat_despesas.models import NatDespesa


@login_required()
def listar_natdespesas(request):
    template_name = 'nat_despesas/listar_natdespesas.html'
    natdespesas = NatDespesa.objects.all()
    context = {
        'natdespesas': natdespesas
    }
    return render(request, template_name, context)


@login_required()
def inserir_natdespesa(request):
    template_name = 'nat_despesas/inserir_natdespesas.html'
    if request.method == 'POST':
        form = NatDespesaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('nat_despesas:listar_natdespesas')
    form = NatDespesaForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required()
def listar_detalhe_natdespesa(request, id):
    template_name = 'nat_despesas/listar_detalhe_natdespesa.html'
    natdespesa = NatDespesa.objects.get(id=id)
    context = {
        'natdespesa': natdespesa
    }
    return render(request, template_name, context)


@login_required()
def editar_natdespesa(request, id):
    template_name = 'nat_despesas/inserir_natdespesas.html'
    natdespesa = NatDespesa.objects.get(id=pk)
    form = NatDespesaForm(request.POST or None, instance=natdespesa)
    context = {
        'form':form
    }
    if form.is_valid():
        form.save()
        return redirect('nat_despesas:listar_natdespesas')
    return render(request, template_name, context)


@login_required
def excluir_natdespesa(request, id):
    natdespesa = NatDespesa.objects.get(id=pk)
    if request.method == "POST":
        natdespesa.delete()
        return redirect('nat_despesas:listar_nat_despesas')
    return render(request, 'nat_despesa/confirma_exclusao.html', {'natdespesa': natdespesa})



"""
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

from weasyprint import HTML


@login_required
def gerar_pdf(request):
    turma = Turma.objects.all().order_by('tur_turma')

    # Rendered
    html_string = render_to_string('turmas/rel_turmas.html', {'turma': turma})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/rel_turmas.pdf')

    fs = FileSystemStorage('/tmp')

    with fs.open('rel_turmas.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        # Faz o download do arquivo PDF
        # response['Content-Disposition'] = 'attachment; filename="rel_tipoqueixaprincipal.pdf"'

        # Abre o PDF direto no navegador
        response['Content-Disposition'] = 'attachment; filename="rel_turmas.pdf"'
    return response
"""