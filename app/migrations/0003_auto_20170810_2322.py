# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20170809_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('balance', models.DecimalField(max_digits=30, decimal_places=5)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='operacion',
            name='destinatario',
            field=models.ForeignKey(to='app.Usuario', related_name='operacion_operaciones_recibidas'),
        ),
        migrations.AlterField(
            model_name='operacion',
            name='remitente',
            field=models.ForeignKey(to='app.Usuario', related_name='operacion_operaciones_realizadas'),
        ),
    ]
