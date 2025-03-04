from django.db import models 

from core.trainy.models import muscles

class Exercicies(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    muscle = models.ManyToManyField(muscles.Muscles)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Exercicie"
        verbose_name_plural = "Exercicies"