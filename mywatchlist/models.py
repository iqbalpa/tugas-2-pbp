from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField() # true = sudah, false = belum
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    release_date = models.DateTimeField()
    review = models.TextField()