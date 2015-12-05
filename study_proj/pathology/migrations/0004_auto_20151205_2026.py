# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathology', '0003_auto_20151123_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='clinical_presentation',
            field=models.TextField(max_length=1000),
        ),
    ]
