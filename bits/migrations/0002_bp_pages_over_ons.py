# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bp_pages',
            name='over_ons',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]