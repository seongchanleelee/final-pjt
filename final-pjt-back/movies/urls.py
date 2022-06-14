from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('get/genre/', views.get_genre),
    path('get/movie/', views.get_movie),
    path('get/movie2/', views.get_movie2),
    path('get/movie3/', views.get_movie3),
    path('', views.index),
    # path('ajax/', views.ajax, name='ajax'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/<int:movieId>', views.recommended, name='recommended'),
]