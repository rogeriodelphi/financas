from django.db import models

from fornecedores.models import Fornecedor
from nat_despesas.models import NatDespesa


class Despesa(models.Model):
    des_natdespesa = models.CharField(max_length=100)
    des_datadespesa = models.DateField('Data Despesa')
    des_valordespesa = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    nat_despesa = models.ForeignKey(NatDespesa, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    des_itensdespesa = models.CharField(max_length=255)
    des_obs = models.TextField()
    des_modalidadecartao = models.CharField(max_length=7)

    def __str__(self):
        return self.des_natdespesa

    class Meta:
        db_table = 'despesa'
        ordering = ['des_natdespesa']
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
