# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_transactionmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
