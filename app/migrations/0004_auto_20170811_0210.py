# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170810_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacion',
            name='moneda',
            field=models.ForeignKey(to='app.Moneda'),
        ),
    ]
