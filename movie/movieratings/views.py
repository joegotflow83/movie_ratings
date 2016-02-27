from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Avg

from .models import Review, Movie, Rater, Post
from .forms import PostForm


class IndexView(View):


	def get(self, request):
		"""Display the top 20 movies"""
		top_movies = Movie.objects.order_by('-rating_average')[:20]
		return render(request, 'movieratings/index.html', {'top_movies': top_movies})


class MovieDetail(View):

    def post(self, request, pk):
        """Allow a user to post a review about a movie"""
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            form.errors

    def get(self, request, pk):
        """Display the movie in detail if clicked on"""
        reviewers = get_list_or_404(Review, movie=pk)
        posters = Post.objects.all()
        movie = Movie.objects.get(id=pk)
        average = Review.objects.filter(movie_id=pk).aggregate(Avg('rating'))
        form = PostForm()
        return render(request, 'movieratings/movie_detail.html',
        			{'reviewers': reviewers,
        			'average': average['rating__avg'],
        			'movie': movie,
        			'posters': posters,
                    'form': form})


class UserDetail(View):


    def get(self, request, pk):
        """Display the users info along with other movies they have rated"""
        info = get_object_or_404(Rater, id=pk)
        movies = get_list_or_404(Review, reviewer=pk)
        print(movies)
        return render(request, 'movieratings/user_detail.html', {'info': info,
                                                                 'movies': movies})


class MovieList(ListView):


	model = Movie
