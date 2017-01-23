# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(default=b'', max_length=100, blank=True)),
                ('apellido', models.CharField(default=b'', max_length=100, blank=True)),
                ('cedula', models.CharField(default=b'', max_length=100, blank=True)),
                ('ciudad', models.CharField(default=b'', max_length=100, blank=True)),
                ('provincia', models.CharField(default=b'', max_length=100, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
