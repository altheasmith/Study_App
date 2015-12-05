# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacology', '0002_auto_20151117_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='spectrum',
        ),
        migrations.AddField(
            model_name='drug',
            name='class_name',
            field=models.CharField(max_length=50, default='class_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='contraindications',
            field=models.TextField(max_length=150, default='contraindications'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='mechanism',
            field=models.TextField(max_length=300, default='mechanism'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drug',
            name='side_effects',
            field=models.TextField(max_length=500),
        ),
    ]
