# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='device',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.Device'),
        ),
    ]
