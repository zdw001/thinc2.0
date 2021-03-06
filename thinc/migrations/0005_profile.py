# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-02 21:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thinc', '0004_auto_20170713_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True, default='')),
                ('bio', models.TextField(blank=True, default='', max_length=500)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
