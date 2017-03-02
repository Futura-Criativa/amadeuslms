# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-01 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_auto_20170228_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mygoals',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mine_goals', to='goals.GoalItem', verbose_name='Goal'),
        ),
    ]