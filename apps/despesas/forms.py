from django import forms
from django.forms import DateInput

from .models import Despesa


class DespesaForm(forms.ModelForm):
    des_itensdespesa = forms.CharField(label='Itens da Despesa', required=False, widget=forms.Textarea(attrs={'rows': '2'}))
    des_obs = forms.CharField(label='Observações', required=False, widget=forms.Textarea(attrs={'rows': '2'}))

    class Meta:
        model = Despesa
        # datetime-local is a HTML5 input type, format to make date time show on fields
        fields = ['des_datadespesa', 'des_valordespesa', 'nat_despesa', 'fornecedor', 'meiodepagamento', 'des_status', 'des_itensdespesa', 'des_obs']
        widgets = {
            'des_datadespesa': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }