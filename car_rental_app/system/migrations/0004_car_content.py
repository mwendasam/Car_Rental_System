# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-29 16:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20160629_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='content',
            field=models.TextField(default=datetime.datetime(2016, 6, 29, 16, 11, 34, 997246, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
