from django.contrib import admin

from .models import Despesa


@admin.register(Despesa)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'des_datadespesa', 'des_valordespesa', 'nat_despesa',
                    'fornecedor', 'meiodepagamento', 'des_itensdespesa']
