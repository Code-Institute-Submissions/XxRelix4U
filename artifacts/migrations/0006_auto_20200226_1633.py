# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-26 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0005_artifact_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifact',
            old_name='price',
            new_name='starting_bid',
        ),
        migrations.AddField(
            model_name='artifact',
            name='time_ending',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='artifact',
            name='time_starting',
            field=models.DateTimeField(null=True),
        ),
    ]