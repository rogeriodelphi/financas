from django import forms

from .models import Fornecedor


class Fornecedor(forms.ModelForm):
    model = Fornecedor
    fields = ['for_fornecedor', 'for_fone']
