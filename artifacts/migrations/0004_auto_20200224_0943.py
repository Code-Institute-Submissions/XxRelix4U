# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-24 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0003_auto_20200222_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='description',
            field=models.TextField(max_length=25),
        ),
    ]
