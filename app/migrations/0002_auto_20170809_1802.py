# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneda',
            name='valor_dolar'
        ),
        migrations.AddField(
            model_name='moneda',
            name='valor_dolar',
            field=models.DecimalField(max_digits=30, decimal_places=5),
        ),
    ]
