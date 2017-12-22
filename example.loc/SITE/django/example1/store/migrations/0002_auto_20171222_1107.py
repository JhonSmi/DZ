# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cathegory',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cathegory',
            name='created',
            field=models.DateTimeField(verbose_name='data created', default=datetime.datetime(2017, 12, 22, 11, 7, 14, 904028)),
        ),
        migrations.AlterField(
            model_name='cathegory',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cathegory',
            name='responser',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
