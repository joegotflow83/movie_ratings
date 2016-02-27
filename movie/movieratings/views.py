from django.shortcuts import render, get_list_or_404, redirect
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
        reviewers = get_list_or_404(Review, movie_id=pk)
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


class UserDetail(DetailView):


	queryset = Rater.objects.all()
	template_name = 'movieratings/user_detail.html'
	
	def get_object(self):
		"""Display the user data when clicked on"""
		object = super().get_object()
		return object


class MovieList(ListView):


	model = Movie
