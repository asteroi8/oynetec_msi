# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-10 11:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0020_auto_20181110_1123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ComponentType',
            new_name='System',
        ),
    ]