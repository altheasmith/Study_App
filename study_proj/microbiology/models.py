from django.db import models

class Bacterium(models.Model):
    SHAPE_CHOICES = (
        ('COCCUS', "Spherical"),
        ('BACILLUS', "Rod-shaped"),
        ('SPIRAL', "Spiral"),
        ('FILAMENTOUS', "Filamentous"),
        ('ARCULA', "Box-shaped"),
        ('APPENDAGED', "Appendaged"),
        ('PLEOMORPHIC', "Pleomorphic")
    )
    AEROBIC_CHOICES=(
        ('AEROBIC', "Aerobic"),
        ('ANAEROBIC', "Anaerobic")
    )
    genus = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    shape = models.CharField(max_length=50, choices=SHAPE_CHOICES)
    aerobic = models.CharField(max_length=50, choices=AEROBIC_CHOICES)
    clinical_presentation = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return ' '.join(self.genus, self.species)
