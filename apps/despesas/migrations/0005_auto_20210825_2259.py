# Generated by Django 3.1.2 on 2021-08-26 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0004_auto_20210825_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='despesa',
            options={'ordering': ['nat_despesa'], 'verbose_name': 'Despesa', 'verbose_name_plural': 'Despesas'},
        ),
    ]
