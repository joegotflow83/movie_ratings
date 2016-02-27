# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 19:03
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import Avg


def add_rating_average(apps, schema_editor):
    Movie = apps.get_model('movieratings', 'Movie')
    Review = apps.get_model('movieratings', 'Review')

    for movie in Movie.objects.all():
        rating_average = Review.objects.filter(movie=movie.pk).aggregate(Avg('rating'))
        movie.rating_average = rating_average['rating__avg']
        movie.save()

class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0012_auto_20160227_1903'),
    ]

    operations = [	
    	migrations.RunPython(add_rating_average)
    ]
