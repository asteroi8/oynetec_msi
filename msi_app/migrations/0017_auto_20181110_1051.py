# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-10 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0016_auto_20181110_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='manufacturer',
            field=models.CharField(max_length=200),
        ),
    ]
