from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/movie_list.html", {"movies" : movies})

@login_required
def add_to_favorites(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_profile.favorite_movies.add(movie)
    return redirect('movie_list')

@login_required
def remove_from_favorites(request, movie_id):
    movie = get_object_or_404(Movie, movie_id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.favorite_movies.remove(movie)
    return redirect('movie_list')

def recommend_movies(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    favorite_movies = user_profile.favorite_movies.all()
    
    recommended_movies = Movie.objects.filter(
        genre__in = [movie.genre for movie in favorite_movies]
    ).exclude(id__in = [movie.id for movie in favorite_movies])
    
    return render(request, 'movies/recommendations.html', {'recommended_movies': recommended_movies})