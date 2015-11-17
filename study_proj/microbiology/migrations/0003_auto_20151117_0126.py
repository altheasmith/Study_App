# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microbiology', '0002_auto_20151116_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fungus',
            old_name='name',
            new_name='genus',
        ),
        migrations.AddField(
            model_name='bacterium',
            name='other_lab_findings',
            field=models.TextField(max_length=500, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fungus',
            name='species',
            field=models.CharField(max_length=50, default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virus',
            name='category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bacterium',
            name='shape',
            field=models.CharField(max_length=50, choices=[(None, "Select the Bacterium's Shape"), ('COCCUS', 'Coccus'), ('BACILLUS', 'Bacillus'), ('SPIRAL', 'Spiral'), ('FILAMENTOUS', 'Filamentous'), ('CURVED', 'Curved'), ('PLEOMORPHIC', 'Pleomorphic')]),
        ),
    ]
