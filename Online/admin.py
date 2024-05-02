from django.contrib import admin
from .models import Profile, Category, Actor, Director, Genre, Movie, MovieShots, Rating, Review

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(Review)
