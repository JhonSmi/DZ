# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('teacher', models.CharField(null=True, max_length=255)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 12, 22, 21, 27, 20, 163756), verbose_name='data created')),
                ('level', models.IntegerField(default=0)),
            ],
        ),
    ]
