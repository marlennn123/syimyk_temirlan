from django.db import models
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)
    first = models.CharField(max_length=33)
    last = models.CharField(33)
    country = models.CharField(max_length=22)


class Category(models.Model):
    name = models.CharField(max_length=16)


class Actor(models.Model):
    name = models.CharField(max_length=16)
    age = models.ImageField()
    description = models.TextField()
    image = models.ImageField()


class Director(models.Model):
    name = models.CharField(max_length=16)
    age = models.ImageField()
    description = models.TextField()
    image = models.ImageField()


class Genre(models.Model):
    name = models.CharField(max_length=16)


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


class MovieShots(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")


class Rating(models.Model):
    value = models.SmallIntegerField(default=0)


class Review(models.Model):
    name = models.CharField(max_length=16)
    text = models.TextField(max_length=100)
    parent = models.ForeignKey(
        'self', verbose_name="", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")

