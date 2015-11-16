from django.db import models


class Bacterium(models.Model):
    SHAPE_CHOICES = (
        (None, "Select the Bacterium's Shape"),
        ('COCCUS', "Spherical"),
        ('BACILLUS', "Rod-shaped"),
        ('SPIRAL', "Spiral"),
        ('FILAMENTOUS', "Filamentous"),
        ('ARCULA', "Box-shaped"),
        ('APPENDAGED', "Appendaged"),
        ('PLEOMORPHIC', "Pleomorphic")
    )
    AEROBIC_CHOICES=(
        (None, "Aerobic or Anaerobic"),
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
        name = str(self.genus + ' ' + self.species)
        return (name)


class Virus(models.Model):
    name = models.CharField(max_length=50)
    clinical_presentation = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Fungus(models.Model):
    name = models.CharField(max_length=50)
    clinical_presentation = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Parasite(models.Model):
    name = models.CharField(max_length=50)
    clinical_presentation = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name
