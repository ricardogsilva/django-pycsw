# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0009_auto_20150710_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='format',
            field=models.CharField(help_text=b'Maps to pycsw:Format', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='source',
            field=models.CharField(help_text=b'Maps to pycsw:Source', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.CharField(help_text=b'Maps to pycsw:Type', max_length=100, null=True, blank=True),
        ),
    ]
