# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathology', '0004_auto_20151205_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalVignette',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('vignette', models.TextField(max_length=2000)),
                ('disease', models.ForeignKey(to='pathology.Disease')),
            ],
        ),
    ]
