# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0006_remove_country_locode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
    ]
