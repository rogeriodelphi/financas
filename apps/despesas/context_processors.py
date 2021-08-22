from django.db.models import Sum

from apps.despesas.models import Despesa, Fornecedor


def despesa_count(request):
    despesa = Despesa.objects.all()
    context = {'total_despesa': despesa.count()}
    return context

def despesa_sum(request):
    despesa = Despesa.objects.all().aggregate(Sum('des_valordespesa'))
    context = {'soma_despesa': despesa}
    return context

def fornecedor_count(request):
    fornecedor = Fornecedor.objects.all()
    context = {'total_fornecedor': fornecedor.count()}
    return context