# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hackers', '0002_auto_20160309_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(max_length=60, unique=True),
        ),
    ]
