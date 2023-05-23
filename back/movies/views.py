from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieDetailSerializer, GenreListSerializer
import requests
from django.conf import settings

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_id):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieDetailSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':

        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        



# # 장르 정보 가져오기
def get_genre(genre_ids):
    genres = Genre.objects.filter(id__in=genre_ids)
    return genres

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def genres_list(request):
    if request.method == 'GET':
        # genress = genres.objects.all()
        genres = get_list_or_404(Genre)
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)