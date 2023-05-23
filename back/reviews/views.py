from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewSerializer
from .models import Review
from movies.models import Movie


@api_view(['GET'])
def review_list(request, movie_id):
    if request.method == 'GET':
        reviews = get_list_or_404(Review, movie_id=movie_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['POST'])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
