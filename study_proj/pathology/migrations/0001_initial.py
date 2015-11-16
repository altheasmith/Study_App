# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('clinical_presentation', models.TextField(max_length=500)),
                ('treatment', models.TextField(max_length=300)),
                ('notes', models.TextField(max_length=500)),
            ],
        ),
    ]
