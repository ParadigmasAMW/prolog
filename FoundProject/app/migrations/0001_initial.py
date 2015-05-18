# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('ID', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=255, null=True, blank=True)),
                ('Category', models.CharField(max_length=255, null=True, blank=True)),
                ('Language', models.CharField(max_length=50, null=True, blank=True)),
                ('License', models.CharField(max_length=50, null=True, blank=True)),
                ('Platform', models.CharField(max_length=50, null=True, blank=True)),
                ('Size', models.CharField(max_length=255, null=True, blank=True)),
                ('Initial_Date', models.CharField(max_length=50, null=True, blank=True)),
                ('Final_Date', models.CharField(max_length=50, null=True, blank=True)),
                ('Value', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]
