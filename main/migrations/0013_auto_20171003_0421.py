# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_pagecategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecategory',
            options={'verbose_name_plural': 'Категории страниц'},
        ),
        migrations.AddField(
            model_name='pagestyleone',
            name='category',
            field=models.ManyToManyField(to='main.PageCategory'),
        ),
    ]
