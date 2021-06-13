from django import forms

from .models import NatDespesa


class NatDespesaForm(forms.ModelForm):
    pro_obs = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': '3'}))

    class Meta:
        model = NatDespesa
        filds = '__all__'
