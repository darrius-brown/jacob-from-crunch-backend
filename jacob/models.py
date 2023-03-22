from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100, default='name')
    description = models.TextField()

    def __str__(self):
        return self.name
