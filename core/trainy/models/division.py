from django.db import models
from core.trainy.models import Workout
from core.trainy.models import muscles

class Division(models.Model):
    name = models.CharField(max_length=45)
    workout = models.ForeignKey(Workout, related_name="divisions", on_delete=models.CASCADE)  # Adicionado o relacionamento com Workout
    muscles = models.ManyToManyField(muscles.Muscles)


    def __str__(self):
        return f"{self.name} - {self.workout.name}"
    
    class Meta:
        verbose_name = "Division"
        verbose_name_plural = "Divisions"


    
    