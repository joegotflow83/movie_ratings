from django.db import models
from django.db.models import Avg


class Rater(models.Model):


        age = models.IntegerField()
        gender = models.CharField(max_length=1)
        occupation = models.CharField(max_length=255)
        zip_code = models.CharField(max_length=10)

        def __str__(self):
                return '{} {} {} {} {}'.format(self.id, self.age, self.gender,
                                                                           self.occupation, self.zip_code)


class Movie(models.Model):


        title = models.CharField(max_length=2000)
        released_date = models.CharField(max_length=4)
        video_release_date = models.CharField(max_length=24, blank=True)
        imdb_url = models.URLField()
        unknown_genre = models.IntegerField(default=0)
        action = models.IntegerField(default=0)
        adventure = models.IntegerField(default=0)
        animation = models.IntegerField(default=0)
        childrens = models.IntegerField(default=0)
        comedy = models.IntegerField(default=0)
        crime = models.IntegerField(default=0)
        documentary = models.IntegerField(default=0)
        drama = models.IntegerField(default=0)
        fantasy = models.IntegerField(default=0)
        filmnoir = models.IntegerField(default=0)
        horror = models.IntegerField(default=0)
        musical = models.IntegerField(default=0)
        mystery = models.IntegerField(default=0)
        romance = models.IntegerField(default=0)
        scifi = models.IntegerField(default=0)
        thriller = models.IntegerField(default=0)
        war = models.IntegerField(default=0)
        western = models.IntegerField(default=0)

        @property
        def average(self):
            return Review.objects.filter(movie=self).aggregate(Avg('rating'))['rating__avg']

        def __str__(self):
                return self.title


class Review(models.Model):


        reviewer = models.ForeignKey(Rater)
        movie = models.ForeignKey(Movie)
        rating = models.IntegerField()
        timestamp = models.IntegerField()

        def __str__(self):
                return '{} {} {} {} {}'.format(self.id, self.reviewer,
                                                                           self.movie, self.rating,
                                                                           self.timestamp)
