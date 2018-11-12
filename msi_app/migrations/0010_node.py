# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0009_auto_20181109_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hostname', models.CharField(max_length=200)),
                ('ipv4', models.CharField(max_length=200)),
                ('ipv6', models.CharField(max_length=200)),
            ],
        ),
    ]