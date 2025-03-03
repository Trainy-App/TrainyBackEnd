from django.db import models
from core.authentication.models.user import User

class Athlete(models.Model):
    weight = models.CharField(max_length=45)
    height = models.CharField(max_length=45)
    imc = models.CharField(max_length=45)
    date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Athlete {self.id}"