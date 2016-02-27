from django.db import models


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
        unknown_genre = models.IntegerField()
        action = models.IntegerField()
        adventure = models.IntegerField()
        animation = models.IntegerField()
        childrens = models.IntegerField()
        comedy = models.IntegerField()
        crime = models.IntegerField()
        documentary = models.IntegerField()
        drama = models.IntegerField()
        fantasy = models.IntegerField()
        filmnoir = models.IntegerField()
        horror = models.IntegerField()
        musical = models.IntegerField()
        mystery = models.IntegerField()
        romance = models.IntegerField()
        scifi = models.IntegerField()
        thriller = models.IntegerField()
        war = models.IntegerField()
        western = models.IntegerField()
        rating_average = models.FloatField()

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
