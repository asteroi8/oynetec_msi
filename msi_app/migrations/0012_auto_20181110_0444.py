# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-10 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0011_hardware_installed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='installed',
            old_name='what',
            new_name='hardware',
        ),
    ]
