from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 영화 기본 기능
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/genres/', views.genres_list, name='genres_list'),
]