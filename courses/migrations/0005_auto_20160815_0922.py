# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 12:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20160728_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'Module', 'verbose_name_plural': 'Modules'},
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateField(auto_now_add=True, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='course',
            name='create_date',
            field=models.DateField(auto_now_add=True, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(verbose_name='End of Course Date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_register_date',
            field=models.DateField(verbose_name='Register Date (End)'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='no_image.jpg', upload_to='courses/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='course',
            name='init_date',
            field=models.DateField(verbose_name='Begin of Course Date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='init_register_date',
            field=models.DateField(verbose_name='Register Date (Begin)'),
        ),
        migrations.AlterField(
            model_name='course',
            name='max_students',
            field=models.PositiveIntegerField(blank=True, verbose_name='Maximum Students'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='objectivies',
            field=models.TextField(blank=True, verbose_name='Objectivies'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='module',
            name='create_date',
            field=models.DateField(auto_now_add=True, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='module',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
        ),
    ]