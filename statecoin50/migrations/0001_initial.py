# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=250)),
                ('stAbbr', models.CharField(max_length=2)),
                ('owned', models.BooleanField(default=False)),
                ('stURL', models.URLField(max_length=250)),
            ],
        ),
    ]