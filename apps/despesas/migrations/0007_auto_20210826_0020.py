# Generated by Django 3.1.2 on 2021-08-26 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0006_auto_20210825_2301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='despesa',
            options={'ordering': ['id', '-des_datadespesa', 'nat_despesa'], 'verbose_name': 'Despesa', 'verbose_name_plural': 'Despesas'},
        ),
    ]
