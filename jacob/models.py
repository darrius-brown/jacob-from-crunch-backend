from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100, default='name')
    category = models.CharField(max_length=100, default='category')
    compound = models.BooleanField(default=True)
    isloation = models.BooleanField(default=True)
    muscle = models.CharField(max_length=100, default='muscle')

    def __str__(self):
        return self.name
    
class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ManyToManyField(Exercise)

    def __str__(self, value=None):
        if value is None:
            return f"{self.user}"
        else:
            return self.user
    
