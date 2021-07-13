from django import forms

from .models import MeiodePagamento


class MeiodePagamento(forms.ModelForm):
    model = MeiodePagamento
    fields = ['mei_meiopagamento', 'mei_obs']
