# Generated by Django 3.1.2 on 2021-07-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_fornecedor', models.CharField(max_length=100, verbose_name='Fornecedor')),
                ('for_fone', models.CharField(max_length=12)),
                ('for_obs', models.TextField()),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'db_table': 'fornecedor',
                'ordering': ['for_fornecedor'],
            },
        ),
    ]
