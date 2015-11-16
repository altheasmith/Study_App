# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bacterium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genus', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('shape', models.CharField(choices=[('COCCUS', 'Spherical'), ('BACILLUS', 'Rod-shaped'), ('SPIRAL', 'Spiral'), ('FILAMENTOUS', 'Filamentous'), ('ARCULA', 'Box-shaped'), ('APPENDAGED', 'Appendaged'), ('PLEOMORPHIC', 'Pleomorphic')], max_length=50)),
                ('aerobic', models.CharField(choices=[('AEROBIC', 'Aerobic'), ('ANAEROBIC', 'Anaerobic')], max_length=50)),
                ('clinical_presentation', models.TextField(max_length=500)),
                ('treatment', models.TextField(max_length=300)),
                ('notes', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Fungus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('clinical_presentation', models.TextField(max_length=500)),
                ('treatment', models.TextField(max_length=300)),
                ('notes', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Parasite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('clinical_presentation', models.TextField(max_length=500)),
                ('treatment', models.TextField(max_length=300)),
                ('notes', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('clinical_presentation', models.TextField(max_length=500)),
                ('treatment', models.TextField(max_length=300)),
                ('notes', models.TextField(max_length=500)),
            ],
        ),
    ]
