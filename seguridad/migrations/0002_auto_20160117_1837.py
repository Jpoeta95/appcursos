# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='alumno_curso',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='alumno_docente',
        ),
        migrations.DeleteModel(
            name='alumno',
        ),
    ]
