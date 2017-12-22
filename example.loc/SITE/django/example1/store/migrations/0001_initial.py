# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cathegory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('responser', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 12, 22, 10, 54, 0, 102581), verbose_name='data created')),
                ('level', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
