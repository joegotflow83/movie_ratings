from django.contrib import admin

from .models import Rater, Movie, Review


admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Review)