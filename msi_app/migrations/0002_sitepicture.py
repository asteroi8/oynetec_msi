# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import msi_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('msi_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=msi_app.models.get_image_path)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_app.Site')),
            ],
        ),
    ]