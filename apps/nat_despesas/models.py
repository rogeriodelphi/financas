from django.db import models


class NatDespesa(models.Model):
    nat_natdespesa = models.CharField('Natureza da Despesa', max_length=100)
    nat_obs = models.TextField('Observações', max_length=300, blank=True, null=True)

    def __str__(self):
        return self.nat_natdespesa

    class Meta:
        db_table = 'natdespesa'
        ordering = ['nat_natdespesa']
        verbose_name = 'Natureza da Despesa'
        verbose_name_plural = 'Naturezas da Despesas'
