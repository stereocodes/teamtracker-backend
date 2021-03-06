# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('SOW', 'Statement of Work / Legal'), ('PRO', 'Project Process'), ('SAL', 'Sales / Marketing'), ('BRA', 'PRPL Brand'), ('HRP', 'HR & Paperwork')], max_length=3)),
                ('filename', models.CharField(max_length=256)),
                ('created', models.DateField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profiles')),
            ],
        ),
    ]
