# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-13 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thinc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]