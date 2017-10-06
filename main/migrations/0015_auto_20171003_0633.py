# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_pagestyletwo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagestyleone',
            name='category',
        ),
        migrations.RemoveField(
            model_name='pagestyletwo',
            name='category',
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='page_one',
            field=models.ManyToManyField(to='main.PageStyleOne', verbose_name='Страница стиль 1'),
        ),
    ]