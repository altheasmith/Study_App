from django.db import models
from microbiology.models import Bacterium, Virus, Fungus, Parasite
from pharmacology.models import Drug
from pathology.models import Disease

class ClinicalVignette(models.Model):
    vignette = models.TextField(max_length=500)
    disease = models.ForeignKey(Disease)
    drug = models.ForeignKey(Drug, null=True)
    bacterium = models.ForeignKey(Bacterium, null=True)
    virus = models.ForeignKey(Virus, null=True)
    fungus = models.ForeignKey(Fungus, null=True)
    parasite = models.ForeignKey(Parasite, null=True)
