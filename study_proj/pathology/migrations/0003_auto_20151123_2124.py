# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathology', '0002_disease_organ_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='morphology',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disease',
            name='pathogenesis',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
