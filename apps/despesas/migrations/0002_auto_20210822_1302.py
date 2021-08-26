# Generated by Django 3.1.2 on 2021-08-22 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nat_despesas', '0001_initial'),
        ('fornecedores', '0001_initial'),
        ('meiodepagamentos', '0001_initial'),
        ('despesas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='des_status',
            field=models.CharField(blank=True, choices=[('1', 'PAGO'), ('2', 'A PAGAR'), ('3', 'VENCIDO')], max_length=1, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='des_valordespesa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fornecedores.fornecedor', verbose_name='Fornecedor'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='meiodepagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meiodepagamentos.meiodepagamento', verbose_name='Meio de Pagamento'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='nat_despesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nat_despesas.natdespesa', verbose_name='Natureza da Despesa'),
        ),
    ]
