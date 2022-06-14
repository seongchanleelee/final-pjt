from django import forms
from .models import Movie, Genre

class GenreForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=50)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('movie_genres', 'movieId', 'genreStr',)    