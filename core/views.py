from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/contas/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/contas/login/')
def charts(request):
    return render(request, 'chartjs.html')

@login_required(login_url='/contas/login/')
def tables(request):
    return render(request, 'basic-table.html')

# def home(request):
#     return render(request, 'home.html')
#
# def dashboard(request):
#     return render(request, 'gerenciais/dashboard.html')
