from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Despesa


@login_required()
def listar_despesas(request):
    template_name = 'despesas/listar_despesas.html'
    despesas = Despesa.objects.all()
    context = {'despesas': despesas}
    return render(request, template_name, context)
