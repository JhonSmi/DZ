# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField()),
                ('attendance', models.CharField(max_length=255)),
                ('studentAttend', models.ForeignKey(null=True, to='store.Student')),
            ],
        ),
    ]
