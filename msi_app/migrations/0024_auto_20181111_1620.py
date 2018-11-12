# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-11 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0023_auto_20181111_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='install',
            name='where',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_app.Site'),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]