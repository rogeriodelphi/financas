from django.urls import path

from .views import (
    listar_despesas,
)

app_name = 'apps.despesas'

urlpatterns = [
    path('', listar_despesas, name='listar_despesas'),
]