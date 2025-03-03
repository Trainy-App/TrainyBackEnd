from django.db import models
from core.trainy.models import Workout

class Division(models.Model):
    name = models.CharField(max_length=45)
    workouts = models.OneToOneField(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.workouts.name}"
    
    class Meta:
        verbose_name = "Division"
        verbose_name_plural = "Divisions"


    
    