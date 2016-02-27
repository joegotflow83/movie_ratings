from django.shortcuts import render, get_list_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Avg
import operator

from .models import Review, Movie, Rater


class IndexView(View):


	def get(self, request):
		"""Grab top 20 movies with the highest ratings"""
		'''average_list = []
		for movie in Movie.objects.all():
			average_list.append((movie.title, (Review.objects.filter(movie=movie).aggregate(Avg('rating')))))
		ratings = []
		for rating in ratings:
			ratings.append((rating[0], rating[1]['rating__avg']))
		top_twenty = sorted(ratings, key=operator.itemgetter(1), reverse=True)[:20]
		for index, number in enumerate(Movie.objects.all()):
			if number.title == top_twenty[index]:'''
		return render(request, 'movieratings/index.html', {})
		#return render(request, 'movieratings/index.html', {'top20': top_twenty})


class MovieDetail(View):


	def get(self, request, pk):
		"""Display the movie in detail if clicked on"""
		reviewers = get_list_or_404(Review, movie_id=pk)
		movie = Movie.objects.get(id=pk)
		average = Review.objects.filter(movie_id=pk).aggregate(Avg('rating'))
		return render(request, 'movieratings/movie_detail.html',
								{'reviewers': reviewers,
								'average': average['rating__avg'],
								'movie': movie})


class UserDetail(DetailView):


	queryset = Rater.objects.all()
	template_name = 'movieratings/user_detail.html'

	def get_object(self):
		"""Display the user data when clicked on"""
		object = super().get_object()
		return object


class MovieList(ListView):


	model = Movie
