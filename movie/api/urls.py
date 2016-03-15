from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^movies/$', views.AllMoviesAPI.as_view(), name='api_movies'),
    url(r'^movies/(?P<pk>\d+)/$', views.MovieAPI.as_view(), name='api_movie'),
    url(r'^users/$', views.AllUsersAPI.as_view(), name='api_users'),
    url(r'^users/(?P<pk>\d+)/$', views.UserAPI.as_view(), name='api_user'),
    url(r'^ratings/$', views.AllRatingsAPI.as_view(), name='api_ratings'),
    url(r'^ratings/(?P<pk>\d+)/$', views.RatingAPI.as_view(), name='api_rating'),
]
