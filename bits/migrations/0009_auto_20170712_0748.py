# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bits', '0008_auto_20170710_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bp_products',
            name='file',
            field=models.FileField(upload_to='document/%Y/'),
        ),
    ]