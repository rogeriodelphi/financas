from django.urls import path

from .views import (
    listar_fornecedores,
    inserir_fornecedor,
    listar_detalhe_fornecedor,
    editar_fornecedor,
    excluir_fornecedor,
)

app_name = 'apps/fornecedores'

urlpatterns = [
    path('', listar_fornecedores, name='listar_fornecedores'),
    path('inserir', inserir_fornecedor, name='inserir_fornecedor'),
    path('listar/<int:id>/', listar_detalhe_fornecedor, name='listar_detalhe_fornecedor'),
    path('editar/<int:id>/', editar_fornecedor, name='editar_fornecedor'),
    path('excluir/<int:id>/', excluir_fornecedor, name='excluir_fornecedor'),
]
