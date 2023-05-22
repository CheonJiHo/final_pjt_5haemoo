from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('movies/<int:movie_id/reviews/', views.review_create),
    path('reviews/', views.review_list),
    path('reviews/<int:movie_id>/', views.review_detail),
]