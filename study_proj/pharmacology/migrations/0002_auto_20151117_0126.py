# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacology', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='use',
        ),
        migrations.AddField(
            model_name='drug',
            name='clinical_uses',
            field=models.TextField(max_length=300, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='spectrum',
            field=models.TextField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
