# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathology', '0001_initial'),
        ('microbiology', '0002_auto_20151116_2009'),
        ('pharmacology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalVignette',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('vignette', models.TextField(max_length=500)),
                ('bacterium', models.ForeignKey(to='microbiology.Bacterium', null=True)),
                ('disease', models.ForeignKey(to='pathology.Disease')),
                ('drug', models.ForeignKey(to='pharmacology.Drug', null=True)),
                ('fungus', models.ForeignKey(to='microbiology.Fungus', null=True)),
                ('parasite', models.ForeignKey(to='microbiology.Parasite', null=True)),
                ('virus', models.ForeignKey(to='microbiology.Virus', null=True)),
            ],
        ),
    ]
