# Generated by Django 3.1.2 on 2021-07-11 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0001_initial'),
        ('nat_despesas', '0001_initial'),
        ('despesas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='des_itensdespesa',
            field=models.CharField(max_length=255, verbose_name='Itens da despesa'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='des_modalidadecartao',
            field=models.CharField(max_length=7, verbose_name='Modalidade Pagamento'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='des_natdespesa',
            field=models.CharField(max_length=100, verbose_name='Natureza da Despesa'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='des_obs',
            field=models.TextField(verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedores.fornecedor', verbose_name='Fornecedor'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='nat_despesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nat_despesas.natdespesa', verbose_name='Natureza da Despesa'),
        ),
    ]
