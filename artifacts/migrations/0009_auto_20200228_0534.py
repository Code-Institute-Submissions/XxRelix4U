# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-28 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0008_auto_20200227_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='starting_bid',
        ),
        migrations.AddField(
            model_name='artifact',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
