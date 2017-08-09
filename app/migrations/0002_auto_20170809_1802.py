# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneda',
            name='valor_dolar',
            field=models.DecimalField(decimal_places=5, max_digits=30),
        ),
    ]
