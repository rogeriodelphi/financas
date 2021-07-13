from django.contrib import admin

from .models import Fornecedor


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'for_fornecedor', 'for_fone']
