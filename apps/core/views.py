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

@login_required(login_url='/contas/login/')
def forms(request):
    return render(request, 'basic_elements.html')

# @login_required(login_url='/contas/login/')
# def dashboard_plus(request):
#     return render(request, 'dashboard_plus.html')


@login_required(login_url='/contas/login/')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/contas/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/contas/login/')
def pages(request):
    return render(request, 'pages.html')


# def home(request):
#     return render(request, 'home.html')
#
# def dashboard(request):
#     return render(request, 'gerenciais/dashboard.html')
