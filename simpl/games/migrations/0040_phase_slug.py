# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-07 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0039_role_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
