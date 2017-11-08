# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0008_auto_20150710_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='hours_of_service',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
