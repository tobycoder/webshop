# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bits', '0004_auto_20170611_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('q', models.IntegerField()),
                ('maat', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
