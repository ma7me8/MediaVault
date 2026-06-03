from django.db import models
from django.utils import timezone


class Genre(models.Model):
    # can not caerte a genra with more than 225 characters
    name = models.CharField(max_length=225)

    # when we print the genre object it will print the name of the genre instead of the object
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=225)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # that's we can make a relationship between movie and gerne
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=1000)
