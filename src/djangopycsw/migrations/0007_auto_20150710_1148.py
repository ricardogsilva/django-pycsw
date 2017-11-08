# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0006_auto_20150710_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='postal_code',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='short_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pycswconfig',
            name='inspire_default_language',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='coupling_type',
            field=models.CharField(help_text=b'Maps to pycsw:CouplingType', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='distance_uom',
            field=models.CharField(help_text=b'Maps to pycsw:DistanceUOM', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='operation',
            field=models.CharField(help_text=b'Maps to pycsw:Operation', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='resource_language',
            field=models.CharField(help_text=b'Maps to pycsw:ResourceLanguage', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='service_type',
            field=models.CharField(help_text=b'Maps to pycsw:ServiceType', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='service_type_version',
            field=models.CharField(help_text=b'Maps to pycsw:ServiceTypeVersion', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='specification_date_type',
            field=models.CharField(help_text=b'Maps to pycsw:SpecificationDateType', max_length=50, null=True, blank=True),
        ),
    ]
