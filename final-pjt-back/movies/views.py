from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator

from movies.serializers import MovieSerializer
from .models import Movie, Genre

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .forms import MovieForm, GenreForm
from pprint import pprint

@api_view(['GET'])
def get_genre(request):
    BASE_URL = 'https://api.themoviedb.org/3'

    path = '/genre/movie/list'
    params = {
        'api_key': 'ca6a2884989d41801567d6d8aa03a8eb',
        'language': 'ko',
    }
    # 2. 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()
    genres = response.get('genres')

    for genre in genres:
        form = GenreForm(genre)
        if form.is_valid():
            genre_id = form.cleaned_data.get('id')
            name = form.cleaned_data.get('name')
            Genre.objects.create(genre_id=genre_id, name = name)
        else:
            print(form.errors)
    return Response(request.data)

@api_view(['GET'])
def get_movie(request):
    # 데이터 정보 초기화
    movies = Movie.objects.all()
    movies.delete()
    # get popular
    BASE_URL = 'https://api.themoviedb.org/3'

    path = '/movie/popular'
    params = {
        'api_key': 'ca6a2884989d41801567d6d8aa03a8eb',
        'language': 'ko',
        'region': 'KR',
    }

    # 2. 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')
    genres_str = ''
    
    for result in results:
        form = MovieForm(result)
        movie = form.save()
        genres_str = '장르: '
        for genre_id in result['genre_ids']:
            genres = Genre.objects.all()
            genre = Genre.objects.get(genre_id = genre_id)
            # print(genre.name)
            genres_str += genre.name + ', ' 
            movie.movie_genres.add(genre)
        movie.movieId = result['id']
        movie.genreStr = genres_str[0:-2]
        if form.is_valid():
            movie.save()
            # print(genres_str)
        else:
            print(form.errors)
    return Response(request.data)

@api_view(['GET'])
def get_movie2(request):
    # 데이터 정보 초기화
    movies = Movie.objects.all()
    # get upcoming
    BASE_URL = 'https://api.themoviedb.org/3'

    # path = '/movie/top_rated'
    path = '/movie/upcoming'
    params = {
        'api_key': 'ca6a2884989d41801567d6d8aa03a8eb',
        'language': 'ko',
        'region': 'KR',
    }

    # 2. 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')
    genres_str = ''
    
    for result in results:
        # 중복 제거
        if Movie.objects.filter(title=result.get("title")): continue

        form = MovieForm(result)
        movie = form.save()
        genres_str = '장르: '
        for genre_id in result['genre_ids']:
            genres = Genre.objects.all()
            genre = Genre.objects.get(genre_id = genre_id)
            # print(genre.name)
            genres_str += genre.name + ', ' 
            movie.movie_genres.add(genre)
        movie.movieId = result['id']
        movie.genreStr = genres_str[0:-2]
        if form.is_valid():
            movie.save()
            # print(genres_str)
        else:
            print(form.errors)
    return Response(request.data)

@api_view(['GET'])
def get_movie3(request):
    # 데이터 정보 초기화
    movies = Movie.objects.all()
    # get upcoming
    BASE_URL = 'https://api.themoviedb.org/3'

    path = '/movie/now_playing'
    params = {
        'api_key': 'ca6a2884989d41801567d6d8aa03a8eb',
        'language': 'ko',
        'region': 'KR',
    }

    # 2. 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')
    genres_str = ''
    pprint(results)
    for result in results:
        # 중복 제거
        if Movie.objects.filter(title=result.get("title")): continue
        
        form = MovieForm(result)
        movie = form.save()
        genres_str = '장르: '
        for genre_id in result['genre_ids']:
            genres = Genre.objects.all()
            genre = Genre.objects.get(genre_id = genre_id)
            # print(genre.name)
            genres_str += genre.name + ', ' 
            movie.movie_genres.add(genre)
        movie.movieId = result['id']
        movie.genreStr = genres_str[0:-2]
        if form.is_valid():
            movie.save()
            # print(genres_str)
        else:
            print(form.errors)
    return Response(request.data)


@api_view(['GET'])
def index(request):
    # BASE_URL = 'https://api.themoviedb.org/3'

    # path = '/movie/popular'
    # params = {
    #     'api_key': 'ca6a2884989d41801567d6d8aa03a8eb',
    #     'language': 'ko',
    #     'region': 'KR',
    # }

    # # 2. 요청 및 응답
    # response = requests.get(BASE_URL + path, params=params).json()
    # results = response.get('results')

    # for item in results:

    #     if Movie.objects.filter(title=item.get("title")): continue
        
    #     Movie(title = item.get("title"), release_date = item.get("release_date"),
    #      vote_average= item.get("vote_average"), overview = item.get("overview"), 
    #      poster_path =item.get("poster_path")).save()

    # 원래 코드 <- 영화를 10개만 가져옴
    movies = Movie.objects.order_by('-vote_average')
    paginator = Paginator(movies,100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    serializer = MovieSerializer(page_obj, many=True)
    
    return Response(serializer.data)

#######################################################
@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def recommended(request, movieId):
    BASE_URL = 'https://api.themoviedb.org/3'

    path = f'/movie/{movieId}/recommendations'
    params = {
        'api_key': 'ca6a2884989d41801567d6d8aa03a8eb',
        'language': 'ko',
    }
    print(path)
    # 2. 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')
    #pprint(results)

    return Response(results)