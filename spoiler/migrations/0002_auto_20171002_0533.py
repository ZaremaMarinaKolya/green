# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoiler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spoiler1',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковое число'),
        ),
        migrations.AddField(
            model_name='spoiler2',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковое число'),
        ),
        migrations.AddField(
            model_name='spoiler3',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковое число'),
        ),
        migrations.AddField(
            model_name='spoilerpage',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковое число'),
        ),
        migrations.AddField(
            model_name='spoilerpagebanner',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковое число'),
        ),
    ]
