from django.db import models
from core.authentication.models import Personal, Athlete
from core.trainy.models.plan import Plan

class Contract(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE)
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Contract {self.id}"

    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"