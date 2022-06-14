from django.db import models

class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    movie_genres = models.ManyToManyField(Genre, related_name="movies")
    movieId = models.IntegerField(null=True)
    genreStr = models.CharField(max_length=50)


