# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microbiology', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bacterium',
            name='aerobic',
            field=models.CharField(max_length=50, choices=[(None, 'Aerobic or Anaerobic'), ('AEROBIC', 'Aerobic'), ('ANAEROBIC', 'Anaerobic')]),
        ),
        migrations.AlterField(
            model_name='bacterium',
            name='shape',
            field=models.CharField(max_length=50, choices=[(None, "Select the Bacterium's Shape"), ('COCCUS', 'Spherical'), ('BACILLUS', 'Rod-shaped'), ('SPIRAL', 'Spiral'), ('FILAMENTOUS', 'Filamentous'), ('ARCULA', 'Box-shaped'), ('APPENDAGED', 'Appendaged'), ('PLEOMORPHIC', 'Pleomorphic')]),
        ),
    ]
