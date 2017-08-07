# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('simbolo', models.TextField()),
                ('valor_dolar', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('importe', models.DecimalField(max_digits=30, decimal_places=5)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('destinatario', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='operacion_operaciones_recibidas')),
                ('moneda', models.OneToOneField(to='app.Moneda')),
                ('remitente', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='operacion_operaciones_realizadas')),
            ],
        ),
    ]
