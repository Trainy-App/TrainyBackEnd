from django.db import models 


class Exercicies(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Exercicie"
        verbose_name_plural = "Exercicies"