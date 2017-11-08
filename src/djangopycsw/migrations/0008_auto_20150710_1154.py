# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0007_auto_20150710_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pycswconfig',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
