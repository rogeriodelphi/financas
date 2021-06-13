from django.contrib import admin

from .models import NatDespesa


@admin.register(NatDespesa)
class NatDespesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nat_natdespesa', 'nat_obs')
