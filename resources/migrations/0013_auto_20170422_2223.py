# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 22:23
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_auto_20170422_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/parker/Sites/prplapi/files/'), upload_to='resources/'),
        ),
    ]