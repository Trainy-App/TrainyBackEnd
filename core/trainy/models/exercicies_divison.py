from django.db import models
from core.trainy.models import exercicies, division

class Exercicies_Division(models.Model):
    exercicie = models.ForeignKey(exercicies.Exercicies, on_delete=models.CASCADE)
    division = models.ForeignKey(division.Division, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    series = models.IntegerField()
    
    def __str__(self):
        return f"{self.exercicie.name} - {self.division.name}"
    
    class Meta:
        verbose_name = "Exercicie Division"
        verbose_name_plural = "Exercicies Divisions"