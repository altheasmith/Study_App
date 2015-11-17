# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathology', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='organ_system',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
