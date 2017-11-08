# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0004_auto_20150708_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='metadata_source',
            field=models.CharField(default=b'local', help_text=b'maps to pycsw:MdSource', max_length=255),
        ),
    ]
