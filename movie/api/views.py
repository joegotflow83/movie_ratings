from django.shortcuts import render
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.views.generic import View
import json

from movieratings.models import Movie, Rater, Review


class AllMoviesAPI(View):
    """All movies api endpoint"""
    def get(self, request):
        movies = list(Movie.objects.all().values())
        json_movies = json.dumps(movies)
        return HttpResponse(json_movies)


class MovieAPI(View):
    """Single movie endpoint"""
    def post(self, request):
        """Create movie over endpoint"""
        title = request.POST['title']
        released_date = request.POST['released_date']
        video_release_date = request.POST['video_released_date']
        imdb_url = request.POST['imdb_url']
        new_movie = Movie(title=title, released_date=released_date,
                          video_release_date=video_release_date, imdb_url=imdb_url)
        new_movie.save()
        movie = model_to_dict(new_movie)
        return HttpResponse(json.dumps(movie), content_type='application/json', status=201)

    def get(self, request, pk):
        movie = list(Movie.objects.filter(pk=pk).values())
        json_movie = json.dumps(movie)
        return HttpResponse(json_movie)


class AllUsersAPI(View):
    """All users api endpoint"""
    def post(self, request):
        """Create user over endpoint"""
        age = request.POST['age']
        gender = request.POST['gender']
        occupation = request.POST['occupation']
        zip_code = request.POST['zip_code']
        new_rater = Rater(age=age, gender=gender, occupation=occupation, zip_code=zip_code)
        new_rater.save()
        return HttpResponse(json.dumps(new_rater), content_type='application/json', status=201)

    def get(self, request):
        users = list(Rater.objects.all().values())
        json_users = json.dumps(users)
        return HttpResponse(json_users)


class UserAPI(View):
    """Single user endpoint"""
    def get(self, request, pk):
        user = list(Rater.objects.filter(pk=pk).values())
        json_user = json.dumps(user)
        return HttpResponse(json_user)


class AllRatingsAPI(View):
    """All ratings endpoint"""
    def get(self, request):
        ratings = list(Review.objects.all().values())
        json_ratings = json.dumps(ratings)
        return HttpResponse(json_ratings)


class RatingAPI(View):
    """Single rating endpoint"""
    def get(self, request, pk):
        rating = list(Review.objects.filter(pk=pk).values())
        json_rating = json.dumps(rating)
        return HttpResponse(json_rating)
