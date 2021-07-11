from django import forms

from .models import Despesa


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = '__all__'
        # fields = ('id', 'des_natdespesa', 'des_natdespesa', 'des_datadespesa', 'des_valordespesa', 'nat_despesa',
        #           'fornecedores', 'des_itensdespesa', 'des_modalidadecartao')
