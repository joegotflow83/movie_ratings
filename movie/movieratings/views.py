from django.shortcuts import render, get_list_or_404
from django.views.generic import View
from django.db.models import Avg
import operator

from .models import Review, Movie


class IndexView(View):


	def get(self, request):
		"""Grab top 20 movies with the highest ratings"""
		average_rating = []
		for item in Movie.objects.all():
			average_rating.append((item.title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
		movie_n_rating = []
		for item in average_rating:
			movie_n_rating.append((item[0], item[1]['rating__avg']))
		top_twenty = sorted(movie_n_rating, key=operator.itemgetter(1), reverse=True)[:20]
		return render(request, 'movieratings/index.html', {'top20': top_twenty})


class TopTwentyDetail(View):


	def get(self, request, pk):
		"""Display the movie in detail if clicked on"""
		reviewers = get_list_or_404(Review, movie_id=pk)
		movie = Movie.objects.get(id=pk)
		average = Review.objects.filter(movie_id=pk).aggregate(Avg('rating'))
		return render(request, 'movieratings/top_movie_detail.html',
								{'reviewers': reviewers,
								'average': average,
								'movie': movie})
