from datetime import datetime
from django.db import models

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(datetime.now())
    title = models.CharField(max_length=150)
    description = models.TextField()