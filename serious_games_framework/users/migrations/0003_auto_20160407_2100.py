# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 21:00
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160314_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='canvas_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
