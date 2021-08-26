from django.db import models


class Fornecedor(models.Model):
    for_fornecedor = models.CharField('Fornecedor', max_length=100)
    for_fone = models.CharField('Telefone', max_length=12, null=True, blank=True)
    for_obs = models.TextField('Observações', null=True, blank=True)

    def __str__(self):
        return self.for_fornecedor

    class Meta:
        db_table = 'fornecedor'
        ordering = ['-for_fornecedor']
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
