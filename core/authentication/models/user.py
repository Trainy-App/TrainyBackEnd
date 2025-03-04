from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=255)
    birth_date = models.DateField('date of birth',null=True, blank=True)
    phone = models.CharField(max_length=11)
    photo_url = models.URLField(null=True, blank=True)

    

    def __str__(self):
        return self.username
