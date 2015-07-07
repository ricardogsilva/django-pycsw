# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(help_text=b'Maps to pycsw:Identifier', max_length=255)),
                ('typename', models.CharField(default=b'gmd:MD_Metadata', help_text=b'Maps to pycsw:Typename', max_length=100)),
                ('schema', models.CharField(default=b'http://www.isotc211.org/2005/gmd', help_text=b'Maps to pycsw:Schema', max_length=100)),
                ('metadata_source', models.CharField(default=b'local', help_text=b'maps to pycsw:MdSource', max_length=255)),
                ('insert_date', models.DateTimeField(help_text=b'Maps to pycsw:InsertDate', auto_now_add=True)),
                ('xml', models.TextField(default=b'<gmd:MD_Metadata xmlns:gmd="http://www.isotc211.org/2005/gmd"/>', help_text=b' Maps to pycsw:XML')),
                ('any_text', models.TextField(help_text=b'Maps to pycsw:AnyText')),
                ('language', models.CharField(default=b'eng', help_text=b'Maps to pycsw:Language', max_length=3)),
                ('title', models.CharField(help_text=b'Maps to pycsw:Title', max_length=255)),
                ('abstract', models.TextField(help_text=b'Maps to pycsw:Abstract', blank=True)),
                ('keywords', models.CharField(help_text=b'Maps to pycsw:Keywords', max_length=255, blank=True)),
                ('keywords_types', models.CharField(help_text=b'Maps to pycsw:Keywordstype', max_length=255, blank=True)),
                ('format', models.CharField(help_text=b'Maps to pycsw:Format', max_length=50)),
                ('source', models.CharField(help_text=b'Maps to pycsw:Source', max_length=50, blank=True)),
                ('date', models.DateTimeField(help_text=b'Maps to pycsw:Date, pycsw:Modified, pycsw:RevisionData, pycsw:CreationDate and pycsw:PublicationDate')),
                ('type', models.CharField(help_text=b'Maps to pycsw:Type', max_length=50)),
                ('bounding_box', models.TextField(help_text=b'Maps to pycsw:BoundingBox')),
                ('crs', models.CharField(help_text=b'Maps to pycsw:CRS', max_length=255)),
                ('alternate_title', models.CharField(help_text=b'Maps to pycsw:AlternateTitle', max_length=255, blank=True)),
                ('organization_name', models.CharField(help_text=b'Maps to pycsw:OrganizationName', max_length=255)),
                ('security_constraints', models.CharField(help_text=b'Maps to pycsw:SecurityConstraints', max_length=255)),
                ('parent_identifier', models.CharField(help_text=b'Maps to pycsw:ParentIdentifier', max_length=255)),
                ('topic_category', models.CharField(help_text=b'Maps to pycsw:TopicCategory', max_length=255)),
                ('resource_language', models.CharField(help_text=b'Maps to pycsw:ResourceLanguage', max_length=30)),
                ('geographic_description_code', models.CharField(help_text=b'Maps to pycsw:GeographicDescriptionCode', max_length=50)),
                ('denominator', models.CharField(help_text=b'Maps to pycsw:Denominator', max_length=255)),
                ('distance_value', models.CharField(help_text=b'Maps to pycsw:DistanceValue', max_length=50)),
                ('distance_uom', models.CharField(help_text=b'Maps to pycsw:DistanceUOM', max_length=30)),
                ('temporal_extent_begin', models.DateTimeField(help_text=b'Maps to pycsw:TempExtent_begin', max_length=255, null=True, blank=True)),
                ('temporal_extent_end', models.DateTimeField(help_text=b'Maps to pycsw:TempExtent_end', max_length=255, null=True, blank=True)),
                ('service_type', models.CharField(help_text=b'Maps to pycsw:ServiceType', max_length=30, blank=True)),
                ('service_type_version', models.CharField(help_text=b'Maps to pycsw:ServiceTypeVersion', max_length=30, blank=True)),
                ('operation', models.CharField(help_text=b'Maps to pycsw:Operation', max_length=30, blank=True)),
                ('coupling_type', models.CharField(help_text=b'Maps to pycsw:CouplingType', max_length=30, blank=True)),
                ('operates_on', models.CharField(help_text=b'Maps to pycsw:OperatesOn', max_length=255, blank=True)),
                ('operates_on_identifier', models.CharField(help_text=b'Maps to pycsw:OperatesOnIdentifier', max_length=255, blank=True)),
                ('operates_on_name', models.CharField(help_text=b'Maps to pycsw:OperatesOnName', max_length=255, blank=True)),
                ('degree', models.CharField(help_text=b'Maps to pycsw:Degree', max_length=255, blank=True)),
                ('access_constraints', models.CharField(help_text=b'Maps to pycsw:AccessConstraints', max_length=255, blank=True)),
                ('other_constraints', models.CharField(help_text=b'Maps to pycsw:OtherConstraints', max_length=255, blank=True)),
                ('classification', models.CharField(help_text=b'Maps to pycsw:Classification', max_length=255, blank=True)),
                ('condition_applying_to_access_and_use', models.CharField(help_text=b'Maps to pycsw:ConditionApplyingToAccessAndUse', max_length=255, blank=True)),
                ('lineage', models.CharField(help_text=b'Maps to pycsw:Lineage', max_length=255, blank=True)),
                ('responsible_party_role', models.CharField(help_text=b'Maps to pycsw:ResponsiblePartyRole', max_length=255, blank=True)),
                ('specification_title', models.CharField(help_text=b'Maps to pycsw:SpecificationTitle', max_length=255, blank=True)),
                ('specification_date', models.DateTimeField(help_text=b'Maps to pycsw:SpecificationDate', null=True, blank=True)),
                ('specification_date_type', models.CharField(help_text=b'Maps to pycsw:SpecificationDateType', max_length=30, blank=True)),
                ('creator', models.CharField(help_text=b'Maps to pycsw:Creator', max_length=255, blank=True)),
                ('publisher', models.CharField(help_text=b'Maps to pycsw:Publisher', max_length=255, blank=True)),
                ('contributor', models.CharField(help_text=b'Maps to pycsw:Contributor', max_length=255, blank=True)),
                ('relation', models.CharField(help_text=b'Maps to pycsw:Relation', max_length=255, blank=True)),
                ('links', models.CharField(help_text=b'Maps to pycsw:Links', max_length=255, blank=True)),
            ],
        ),
    ]
