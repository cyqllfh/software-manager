# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0010_script_is_run'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='is_dispatch',
        ),
    ]
