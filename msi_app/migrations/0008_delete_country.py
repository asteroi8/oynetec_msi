# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0007_remove_location_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
    ]