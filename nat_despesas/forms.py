from django import forms

from .models import NatDespesa


class NatDespesaForm(forms.ModelForm):
    nat_obs = forms.CharField(label='Observações', required=False, widget=forms.Textarea(attrs={'rows': '3'}))

    class Meta:
        model = NatDespesa
        fields = '__all__'
