# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-22 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0022_auto_20181206_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='vision',
            field=models.SmallIntegerField(default=3, help_text='How many units ahead of the most recently completed unit the student can see.'),
        ),
        migrations.AlterField(
            model_name='student',
            name='track',
            field=models.CharField(choices=[('A', 'Weekly'), ('B', 'Biweekly'), ('C', 'Correspondence'), ('E', 'External'), ('G', 'Graduate'), ('N', 'Not applicable')], max_length=5),
        ),
    ]
