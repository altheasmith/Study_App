from django.db import models


class Bacterium(models.Model):
    SHAPE_CHOICES = (
        (None, "Select the Bacterium's Shape"),
        ('COCCUS', "Coccus"),
        ('BACILLUS', "Bacillus"),
        ('SPIRAL', "Spiral"),
        ('FILAMENTOUS', "Filamentous"),
        ('CURVED', "Curved"),
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
    other_lab_findings = models.TextField(max_length=500)
    clinical_presentation = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        name = str(self.genus + ' ' + self.species)
        return (name)


class Virus(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    clinical_presentation = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Fungus(models.Model):
    genus = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    clinical_presentation = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        name = str(self.genus + ' ' + self.species)
        return (name)



class Parasite(models.Model):
    name = models.CharField(max_length=50)
    clinical_presentation = models.TextField(max_length=500)
    treatment = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name
