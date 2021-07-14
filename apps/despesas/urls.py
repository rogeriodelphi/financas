from django.urls import path

from .views import (
    listar_despesas,
    inserir_despesa,
)

app_name = 'apps.despesas'

urlpatterns = [
    path('', listar_despesas, name='listar_despesas'),
    path('inserir', inserir_despesa, name='inserir_despesa'),
]