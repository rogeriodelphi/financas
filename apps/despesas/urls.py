from django.urls import path

from .views import (
    listar_despesas,
    inserir_despesa,
    editar_despesa,
    excluir_despesa,
)

app_name = 'despesas'

urlpatterns = [
    path('', listar_despesas, name='listar_despesas'),
    path('inserir', inserir_despesa, name='inserir_despesa'),
    path('editar/<int:id>/', editar_despesa, name='editar_despesa'),
    path('excluir/<int:id>', excluir_despesa, name='excluir_despesa'),
]
