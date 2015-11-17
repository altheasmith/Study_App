from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=50)
    spectrum = models.TextField(max_length=100)
    clinical_uses = models.TextField(max_length=300)
    side_effects = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name
