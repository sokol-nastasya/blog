# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Відео', 'verbose_name_plural': 'Відео'},
        ),
    ]
