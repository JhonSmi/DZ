# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('teacher', models.CharField(null=True, max_length=255)),
                ('datetime', models.CharField(null=True, max_length=255)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fioStudent', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('healthGroup', models.IntegerField(default=0)),
                ('sectionStudent', models.ForeignKey(null=True, to='store.Section')),
            ],
        ),
    ]
