from django import forms

from .models import Despesa


class DespesaForm(forms.ModelForm):
    des_itensdespesa = forms.CharField(label='Observações', required=False, widget=forms.Textarea(attrs={'rows': '3'}))
    des_obs = forms.CharField(label='Observações', required=False, widget=forms.Textarea(attrs={'rows': '3'}))
    class Meta:
        model = Despesa
        fields = ['des_datadespesa', 'des_valordespesa', 'nat_despesa', 'fornecedor', 'meiodepagamento', 'des_status', 'des_itensdespesa', 'des_obs']
