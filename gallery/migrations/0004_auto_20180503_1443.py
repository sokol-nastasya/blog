# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180503_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/gallery_img'),
        ),
    ]
