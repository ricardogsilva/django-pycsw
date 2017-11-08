# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopycsw', '0002_auto_20150707_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pycswconfig',
            options={'verbose_name': 'PyCSW Configuration', 'verbose_name_plural': 'PyCSW Configuration'},
        ),
        migrations.RemoveField(
            model_name='organization',
            name='contact_country',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='contact_postal_code',
        ),
        migrations.AddField(
            model_name='organization',
            name='country',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='postal_code',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='contact_instructions',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='fax',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='hours_of_service',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='phone',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='city',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='state_or_province',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='pycswconfig',
            name='transactions',
            field=models.BooleanField(default=False, help_text=b'Enable transactions'),
        ),
    ]
