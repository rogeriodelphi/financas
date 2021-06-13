from django.urls import path
from .views import listar_natdespesas

urlpatterns = [
    path('listar', listar_natdespesas, name = 'listar_natdespesas'),
    # path('inserir', inserir_natdespesa, name = 'inserir_natdespesa'),
    # path('listar/<int:id>/', listar_natdespesa_id, name = 'listar_natdespesa_id'),
    # path('editar/<int:id>/', editar_natdespesa_id, name = 'editar_natdespesa_id'),
    # path('excluir/<int:id>/', excluir_natdespesa_id, name = 'excluir_natdespesa_id'),
    # path('relatorio', gerarpdf_natdespesas, name='gerarpdf_natdespesas'),
]
