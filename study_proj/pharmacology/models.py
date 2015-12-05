from django.db import models

class Drug(models.Model):
    class_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mechanism = models.TextField(max_length=300)
    clinical_uses = models.TextField(max_length=300)
    side_effects = models.TextField(max_length=500)
    contraindications = models.TextField(max_length=150)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name
