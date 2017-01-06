# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-06 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_register', models.BooleanField(default=False, verbose_name="Don't allow users to self-register")),
                ('maintence', models.BooleanField(default=False, verbose_name='Put system in maintence mode')),
            ],
            options={
                'verbose_name': 'Security configuration',
                'verbose_name_plural': 'Security configurations',
            },
        ),
    ]
