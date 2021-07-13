from django.db import models


class MeiodePagamento(models.Model):
    mei_meiopagamento = models.CharField('Maio de Pagamento', max_length=30)
    mei_obs = models.TextField('Observações', null=True, blank=True)

    def __str__(self):
        return self.mei_meiopagamento

    class Meta:
        db_table = 'meiodepagamento'
        ordering = ['mei_meiopagamento']
        verbose_name = 'Meio de Pagamento'
        verbose_name_plural = 'Meios de Pagamentos'
