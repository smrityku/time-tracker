# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-18 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0005_auto_20180716_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='total_hours',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
