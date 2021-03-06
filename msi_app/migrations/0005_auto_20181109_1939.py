# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0004_auto_20181109_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='locode',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='msi_app.Country'),
            preserve_default=False,
        ),
    ]
