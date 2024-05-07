from django.db import models
from django.contrib.auth.models import User
from datetime import date


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=255)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.user} | {self.country}'

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=16)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=16)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.TextField(max_length=33)
    tagline = models.CharField( max_length=100, default=0)
    description = models.TextField()
    poster = models.ImageField(upload_to="movies")
    year = models.IntegerField()
    country = models.CharField
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_direct")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField( default=0, help_text=0)
    fess_in_world = models.PositiveIntegerField(
        "Сборы в мире", default=0, help_text="указывать сумму в долларах"
    )
    category = models.ForeignKey(on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title


class MovieShots(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
    star = models.IntegerField(choices=[(i, str(i)) for i in range(1,11)], help_text='Оценка', verbose_name='Rating')
    def __str__(self):
        return f'{self.user} | {self.movies}'



class Review(models.Model):
    name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"