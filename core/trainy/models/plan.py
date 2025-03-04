from django.db import models
from core.authentication.models import Personal

class Plan(models.Model):
    price = models.CharField(max_length=45)
    duration = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Plan {self.name} - {self.personal.name}"
    
    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"