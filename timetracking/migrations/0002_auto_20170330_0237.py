# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetrackers',
            name='timer',
            field=models.CharField(max_length=96),
        ),
    ]