from django.contrib import admin

from .models import MeiodePagamento


@admin.register(MeiodePagamento)
class MeiodePagamentoAdmin(admin.ModelAdmin):
    list_display = ['mei_meiopagamento']
