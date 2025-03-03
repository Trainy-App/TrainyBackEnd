from django.db import models
from core.authentication.models import Athlete

class Workout(models.Model):
    name = models.CharField(max_length=45)
    date = models.DateField()
    description = models.CharField(max_length=255)
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE)

    def __str__(self):
        return f"Workout {self.id} - {self.name} - {self.date} - {self.description} - {self.athlete}"

    class Meta:
        verbose_name = "Workout"
        verbose_name_plural = "Workouts"