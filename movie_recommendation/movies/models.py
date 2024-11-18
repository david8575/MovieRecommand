from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    
    def __ini__(self):
        return self.title