# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpl', '0002_runuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='runuser',
            options={'verbose_name': 'run user', 'verbose_name_plural': 'run users'},
        ),
    ]
