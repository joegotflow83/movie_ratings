from django.shortcuts import render, get_list_or_404
from django.views.generic import View
from django.db.models import Avg

from .models import Review, Movie


class IndexView(View):


	def get(self, request):
		"""Grab top 20 movies with the highest ratings"""
		#popular_movies = Review.objects.annotate(Avg('rating')).order_by('-rating')[:20]
		average_list = []
		for x in Movie.objects.all():
			average_list.append(Review.objects.filter(movie=x).aggregate(Avg('rating')))
		top20 = sorted(average_list, key=lambda k: k['avg__rating'])
		return render(request, 'movieratings/index.html', {'top20': top20[:20]})


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
