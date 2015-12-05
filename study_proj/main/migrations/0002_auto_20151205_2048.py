# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicalvignette',
            name='bacterium',
        ),
        migrations.RemoveField(
            model_name='clinicalvignette',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='clinicalvignette',
            name='drug',
        ),
        migrations.RemoveField(
            model_name='clinicalvignette',
            name='fungus',
        ),
        migrations.RemoveField(
            model_name='clinicalvignette',
            name='parasite',
        ),
        migrations.RemoveField(
            model_name='clinicalvignette',
            name='virus',
        ),
        migrations.AlterField(
            model_name='clinicalvignette',
            name='vignette',
            field=models.TextField(max_length=2000),
        ),
    ]
