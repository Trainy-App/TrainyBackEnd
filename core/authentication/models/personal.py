from django.db import models
from core.authentication.models.user import User

class Personal(models.Model):
    cref = models.CharField(max_length=45)
    specialty = models.CharField(max_length=45)
    personalcol = models.CharField(max_length=45)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - CREF: {self.cref}"