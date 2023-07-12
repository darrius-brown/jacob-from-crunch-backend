from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100, default='name')
    category = models.CharField(max_length=100, default='category')
    muscle = models.CharField(max_length=100, default='muscle')
    muscle_joint_group = models.CharField(max_length=100, default='none')
    difficulty = models.CharField(max_length=20, default='Beginner')
    beginner_reps = models.CharField(max_length=20, default='2 x 10')
    intermediate_reps = models.CharField(max_length=20, default='3 x 10')

    def __str__(self):
        return self.name
    
class Program(models.Model):
    day = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ManyToManyField(Exercise)
    experience = models.CharField(max_length=20, default='Beginner')
    
    def __str__(self, value=None):
        if value is None:
            return f"{self.user}"
        else:
            return self.user
    
