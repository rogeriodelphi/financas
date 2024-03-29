# Generated by Django 3.1.2 on 2021-08-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeiodePagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mei_meiopagamento', models.CharField(max_length=30, verbose_name='Maio de Pagamento')),
                ('mei_obs', models.TextField(blank=True, null=True, verbose_name='Observações')),
            ],
            options={
                'verbose_name': 'Meio de Pagamento',
                'verbose_name_plural': 'Meios de Pagamentos',
                'db_table': 'meiodepagamento',
                'ordering': ['mei_meiopagamento'],
            },
        ),
    ]
