from django.urls import path

from .views import (
    listar_despesas,
    inserir_despesa,
    listar_detalhe_despesa,
    editar_despesa,
    excluir_despesa,
    rel_despesas,
)

app_name = 'apps/despesas'

urlpatterns = [
    path('', listar_despesas, name='listar_despesas'),
    path('inserir', inserir_despesa, name='inserir_despesa'),
    path('listar/<int:id>/', listar_detalhe_despesa, name='listar_detalhe_despesa'),
    path('editar/<int:id>/', editar_despesa, name='editar_despesa'),
    path('excluir/<int:id>', excluir_despesa, name='excluir_despesa'),
    path('rel_despesas', rel_despesas, name='rel_despesas'),
    # path('consultar', consultar_despesas, name='consultar_despesas'),
]
