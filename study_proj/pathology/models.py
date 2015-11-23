from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=50)
    clinical_presentation = models.TextField(max_length=500)
    organ_system = models.CharField(max_length=50)
    pathogenesis = models.TextField(max_length=1000)
    morphology = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name
