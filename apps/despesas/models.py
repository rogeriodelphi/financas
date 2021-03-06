from django.db import models

from apps.fornecedores.models import Fornecedor
from apps.meiodepagamentos.models import MeiodePagamento
from apps.nat_despesas.models import NatDespesa


class Despesa(models.Model):
    STATUS_CHOICES = (
        ('1', 'PAGO'),
        ('2', 'A PAGAR'),
        ('3', 'VENCIDO'),
    )

    des_datadespesa = models.DateField('Data Despesa')
    des_valordespesa = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    nat_despesa = models.ForeignKey(NatDespesa, on_delete=models.CASCADE, verbose_name='Natureza da Despesa')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='Fornecedor')
    meiodepagamento = models.ForeignKey(MeiodePagamento, on_delete=models.CASCADE, verbose_name='Meio de Pagamento')
    des_status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES)
    des_itensdespesa = models.TextField('Itens da despesa', max_length=255, null=True, blank=True)
    des_obs = models.TextField('Observações', null=True, blank=True)

    def __str__(self):
        return self.des_obs

    class Meta:
        db_table = 'despesa'
        ordering = ['nat_despesa']
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
