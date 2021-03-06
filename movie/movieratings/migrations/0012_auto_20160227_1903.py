# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0011_auto_20160227_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('rating', models.IntegerField()),
                ('post', models.CharField(max_length=512)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating_average',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
