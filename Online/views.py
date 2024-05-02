from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile, Category, Actor, Director, Genre, Movie, MovieShots, Rating, Review


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'



class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'  # Your template name
    context_object_name = 'movie'


def submit_rating(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        rating_value = request.POST.get('rating')  # Assuming you have a form field named 'rating'


def submit_review(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        review_text = request.POST.get('review')  # Assuming you have a form field named 'review'

