from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import path
from .utils import fetch_movies_from_tmdb

@login_required
def home(request):
    def preprocess_movies(movies):
        for movie in movies:
            # Ensure a safe display title
            movie["display_title"] = movie.get("title") or movie.get("name") or "Untitled"
            # Optional: handle missing rating
            movie["display_rating"] = movie.get("vote_average", "N/A")
        return movies

    trending = fetch_movies_from_tmdb("trending/movie/week")
    now_playing = fetch_movies_from_tmdb("movie/now_playing")
    upcoming = fetch_movies_from_tmdb("movie/upcoming")

    context = {
        "trending": preprocess_movies(trending.get("results", [])),
        "now_playing": preprocess_movies(now_playing.get("results", [])),
        "upcoming": preprocess_movies(upcoming.get("results", [])),
    }

    return render(request, "movies_app/home.html", context)




def custom_logout(request):
    logout(request)
    return redirect('login')

