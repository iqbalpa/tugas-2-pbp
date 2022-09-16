from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField() # true = sudah, false = belum
    title = models.CharField(max_length=255)
    rating = models.IntegerField(min=1, max=5)
    release_date = models.DateTimeField()
    review = models.TextField()