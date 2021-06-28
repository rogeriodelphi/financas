from django.urls import path

from .views import (
    listar_natdespesas,
    inserir_natdespesa,
    listar_detalhe_natdespesa,
    editar_natdespesa,
    excluir_natdespesa,
)

app_name = 'nat_despesas'

urlpatterns = [
    path('', listar_natdespesas, name='listar_natdespesas'),
    path('inserir', inserir_natdespesa, name='inserir_natdespesa'),
    path('listar/<int:id>/', listar_detalhe_natdespesa, name = 'listar_detalhe_natdespesa'),
    path('editar/<int:id>/', editar_natdespesa, name = 'editar_natdespesa'),
    path('excluir/<int:id>/', excluir_natdespesa, name = 'excluir_natdespesa'),
    # path('relatorio', gerarpdf_natdespesas, name='gerarpdf_natdespesas'),
]
