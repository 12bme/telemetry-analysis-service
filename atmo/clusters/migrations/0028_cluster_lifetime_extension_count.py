# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-03 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0027_cluster_lifetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='lifetime_extension_count',
            field=models.PositiveSmallIntegerField(default=0, help_text='Number of lifetime extensions.'),
        ),
    ]
