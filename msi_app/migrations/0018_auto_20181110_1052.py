# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-10 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0017_auto_20181110_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_app.Supplier'),
        ),
    ]