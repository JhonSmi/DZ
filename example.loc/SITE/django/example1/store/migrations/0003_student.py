# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20171224_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fioStudent', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('healthGroup', models.IntegerField(default=0)),
                ('sectionStudent', models.ForeignKey(null=True, to='store.Section')),
            ],
        ),
    ]
