# Generated by Django 3.1.2 on 2021-08-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NatDespesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nat_natdespesa', models.CharField(max_length=100, verbose_name='Natureza da Despesa')),
                ('nat_obs', models.TextField(blank=True, max_length=300, null=True, verbose_name='Observações')),
            ],
            options={
                'verbose_name': 'Natureza da Despesa',
                'verbose_name_plural': 'Naturezas da Despesas',
                'db_table': 'natdespesa',
                'ordering': ['nat_natdespesa'],
            },
        ),
    ]
