# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdocente', '0002_docente_docente_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='docente_curso',
            field=models.ManyToManyField(blank=True, to='aplicurso.curso'),
        ),
    ]
