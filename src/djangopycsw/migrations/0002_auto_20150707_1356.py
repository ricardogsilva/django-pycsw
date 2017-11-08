# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField(blank=True)),
                ('phone', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('hours_of_service', models.CharField(max_length=50)),
                ('contact_instructions', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('state_or_province', models.CharField(max_length=50)),
                ('contact_postal_code', models.CharField(max_length=30)),
                ('contact_country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PycswConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default=b'en-US', max_length=10)),
                ('max_records', models.IntegerField(default=10)),
                ('transactions', models.BooleanField(default=False)),
                ('allowed_ips', models.CharField(default=b'127.0.0.1', help_text=b'IP addresses that are allowed to make transaction requests', max_length=255, blank=True)),
                ('harvest_page_size', models.IntegerField(default=10)),
                ('title', models.CharField(max_length=50)),
                ('abstract', models.TextField()),
                ('keywords', models.CharField(max_length=255)),
                ('keywords_type', models.CharField(max_length=255)),
                ('fees', models.CharField(max_length=100)),
                ('access_constraints', models.CharField(max_length=255)),
                ('repository_filter', models.CharField(max_length=255, blank=True)),
                ('inspire_enabled', models.BooleanField(default=False)),
                ('inspire_languages', models.CharField(max_length=255, blank=True)),
                ('inspire_default_language', models.CharField(max_length=30, blank=True)),
                ('inspire_date', models.DateTimeField(null=True, blank=True)),
                ('gemet_keywords', models.CharField(max_length=255, blank=True)),
                ('conformity_service', models.CharField(max_length=255, blank=True)),
                ('temporal_extent_start', models.DateTimeField(null=True, blank=True)),
                ('temporal_extent_end', models.DateTimeField(null=True, blank=True)),
                ('point_of_contact', models.ForeignKey(to='djangopycsw.Collaborator')),
            ],
        ),
        migrations.AddField(
            model_name='collaborator',
            name='organization',
            field=models.ForeignKey(related_name='collaborators', to='djangopycsw.Organization'),
        ),
    ]
