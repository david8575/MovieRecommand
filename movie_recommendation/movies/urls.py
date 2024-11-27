from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('add_favorite/<int:movie_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_favorite/<int:movie_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('recommendations/', views.recommend_movies, name='recommend_movies'),

]