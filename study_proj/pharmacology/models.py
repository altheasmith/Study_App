from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=50)
    use = models.TextField(max_length=500)
    side_effects = models.TextField(max_length=300)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.name
