# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20170322_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
