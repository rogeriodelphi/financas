# Generated by Django 3.1.2 on 2021-07-11 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedores', '0001_initial'),
        ('nat_despesas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_natdespesa', models.CharField(max_length=100)),
                ('des_datadespesa', models.DateField(verbose_name='Data Despesa')),
                ('des_valordespesa', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('des_itensdespesa', models.CharField(max_length=255)),
                ('des_obs', models.TextField()),
                ('des_modalidadecartao', models.CharField(max_length=7)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedores.fornecedor')),
                ('nat_despesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nat_despesas.natdespesa')),
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
                'db_table': 'despesa',
                'ordering': ['des_natdespesa'],
            },
        ),
    ]
