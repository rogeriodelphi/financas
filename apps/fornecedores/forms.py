from django import forms

from .models import Fornecedor


class FornecedorForm(forms.ModelForm):
    for_obs = forms.CharField(label='Observações', required=False, widget=forms.Textarea(attrs={'rows': '3'}))

    class Meta:
        model = Fornecedor
        fields = ['for_fornecedor', 'for_fone', 'for_obs']
