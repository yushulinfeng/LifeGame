# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-03 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LifeGame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='room',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]