# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-01 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_questoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='enunciado',
            field=models.TextField(blank=True, verbose_name='Statement'),
        ),
    ]
