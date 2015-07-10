# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0005_auto_20150708_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='bounding_box',
            field=models.TextField(help_text=b'Maps to pycsw:BoundingBox', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='crs',
            field=models.CharField(help_text=b'Maps to pycsw:CRS', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(help_text=b'Maps to pycsw:Date, pycsw:Modified, pycsw:RevisionData, pycsw:CreationDate and pycsw:PublicationDate', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='denominator',
            field=models.CharField(help_text=b'Maps to pycsw:Denominator', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='distance_uom',
            field=models.CharField(help_text=b'Maps to pycsw:DistanceUOM', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='distance_value',
            field=models.CharField(help_text=b'Maps to pycsw:DistanceValue', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='format',
            field=models.CharField(help_text=b'Maps to pycsw:Format', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='geographic_description_code',
            field=models.CharField(help_text=b'Maps to pycsw:GeographicDescriptionCode', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='identifier',
            field=models.CharField(help_text=b'Maps to pycsw:Identifier', max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='language',
            field=models.CharField(default=b'eng', max_length=3, null=True, help_text=b'Maps to pycsw:Language', blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='metadata_source',
            field=models.CharField(default=b'local', help_text=b'maps to pycsw:MdSource', max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='organization_name',
            field=models.CharField(help_text=b'Maps to pycsw:OrganizationName', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='parent_identifier',
            field=models.CharField(help_text=b'Maps to pycsw:ParentIdentifier', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='resource_language',
            field=models.CharField(help_text=b'Maps to pycsw:ResourceLanguage', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='schema',
            field=models.CharField(default=b'http://www.isotc211.org/2005/gmd', help_text=b'Maps to pycsw:Schema', max_length=100, db_index=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='security_constraints',
            field=models.CharField(help_text=b'Maps to pycsw:SecurityConstraints', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='topic_category',
            field=models.CharField(help_text=b'Maps to pycsw:TopicCategory', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.CharField(help_text=b'Maps to pycsw:Type', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='typename',
            field=models.CharField(default=b'gmd:MD_Metadata', help_text=b'Maps to pycsw:Typename', max_length=100, db_index=True),
        ),
    ]
