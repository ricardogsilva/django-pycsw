# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0003_auto_20150707_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='abstract',
            field=models.TextField(help_text=b'Maps to pycsw:Abstract', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='access_constraints',
            field=models.CharField(help_text=b'Maps to pycsw:AccessConstraints', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='alternate_title',
            field=models.CharField(help_text=b'Maps to pycsw:AlternateTitle', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='bounding_box',
            field=models.TextField(help_text=b'Maps to pycsw:BoundingBox', null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='classification',
            field=models.CharField(help_text=b'Maps to pycsw:Classification', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='condition_applying_to_access_and_use',
            field=models.CharField(help_text=b'Maps to pycsw:ConditionApplyingToAccessAndUse', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='contributor',
            field=models.CharField(help_text=b'Maps to pycsw:Contributor', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='coupling_type',
            field=models.CharField(help_text=b'Maps to pycsw:CouplingType', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='creator',
            field=models.CharField(help_text=b'Maps to pycsw:Creator', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='crs',
            field=models.CharField(help_text=b'Maps to pycsw:CRS', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(help_text=b'Maps to pycsw:Date, pycsw:Modified, pycsw:RevisionData, pycsw:CreationDate and pycsw:PublicationDate', null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='degree',
            field=models.CharField(help_text=b'Maps to pycsw:Degree', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='denominator',
            field=models.CharField(help_text=b'Maps to pycsw:Denominator', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='distance_uom',
            field=models.CharField(help_text=b'Maps to pycsw:DistanceUOM', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='distance_value',
            field=models.CharField(help_text=b'Maps to pycsw:DistanceValue', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='format',
            field=models.CharField(help_text=b'Maps to pycsw:Format', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='geographic_description_code',
            field=models.CharField(help_text=b'Maps to pycsw:GeographicDescriptionCode', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='keywords',
            field=models.CharField(help_text=b'Maps to pycsw:Keywords', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='keywords_types',
            field=models.CharField(help_text=b'Maps to pycsw:Keywordstype', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='language',
            field=models.CharField(default=b'eng', max_length=3, null=True, help_text=b'Maps to pycsw:Language'),
        ),
        migrations.AlterField(
            model_name='record',
            name='lineage',
            field=models.CharField(help_text=b'Maps to pycsw:Lineage', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='links',
            field=models.CharField(help_text=b'Maps to pycsw:Links', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='metadata_source',
            field=models.CharField(default=b'local', max_length=255, null=True, help_text=b'maps to pycsw:MdSource', blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='operates_on',
            field=models.CharField(help_text=b'Maps to pycsw:OperatesOn', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='operates_on_identifier',
            field=models.CharField(help_text=b'Maps to pycsw:OperatesOnIdentifier', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='operates_on_name',
            field=models.CharField(help_text=b'Maps to pycsw:OperatesOnName', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='operation',
            field=models.CharField(help_text=b'Maps to pycsw:Operation', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='organization_name',
            field=models.CharField(help_text=b'Maps to pycsw:OrganizationName', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='other_constraints',
            field=models.CharField(help_text=b'Maps to pycsw:OtherConstraints', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='parent_identifier',
            field=models.CharField(help_text=b'Maps to pycsw:ParentIdentifier', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='publisher',
            field=models.CharField(help_text=b'Maps to pycsw:Publisher', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='relation',
            field=models.CharField(help_text=b'Maps to pycsw:Relation', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='resource_language',
            field=models.CharField(help_text=b'Maps to pycsw:ResourceLanguage', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='responsible_party_role',
            field=models.CharField(help_text=b'Maps to pycsw:ResponsiblePartyRole', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='security_constraints',
            field=models.CharField(help_text=b'Maps to pycsw:SecurityConstraints', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='service_type',
            field=models.CharField(help_text=b'Maps to pycsw:ServiceType', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='service_type_version',
            field=models.CharField(help_text=b'Maps to pycsw:ServiceTypeVersion', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='source',
            field=models.CharField(help_text=b'Maps to pycsw:Source', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='specification_date_type',
            field=models.CharField(help_text=b'Maps to pycsw:SpecificationDateType', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='specification_title',
            field=models.CharField(help_text=b'Maps to pycsw:SpecificationTitle', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='title',
            field=models.CharField(help_text=b'Maps to pycsw:Title', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='topic_category',
            field=models.CharField(help_text=b'Maps to pycsw:TopicCategory', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.CharField(help_text=b'Maps to pycsw:Type', max_length=50, null=True),
        ),
    ]
