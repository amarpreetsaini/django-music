# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20160917_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='added_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='data added'),
            preserve_default=False,
        ),
    ]