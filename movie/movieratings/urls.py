from django.conf.urls import url

from movieratings import views


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.TopTwentyDetail.as_view(), name='top_twenty_detail')
]