# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-22 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20170319_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='kitId',
            field=models.CharField(default='1111000000', max_length=8, unique=True),
        ),
    ]
