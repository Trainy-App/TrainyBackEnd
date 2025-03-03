from django.db import models
from core.trainy.models import exercicies, division

class Muscles(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    exercicies = models.ManyToManyField(exercicies.Exercicies)
    divisions = models.ManyToManyField(division.Division)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Muscle"
        verbose_name_plural = "Muscles"