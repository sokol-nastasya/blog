# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20180503_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
    ]
