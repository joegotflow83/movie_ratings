from django.conf.urls import url

from movieratings import views


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.MovieDetail.as_view(), name='movie_detail'),
	url(r'^movies/$', views.MovieList.as_view(), name='movie_list'),
	url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user_detail'),
]