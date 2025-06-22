from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import path

from movies_app.models import *
from .utils import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def home(request):
    trending = fetch_movies_from_tmdb("trending/movie/week")
    now_playing = fetch_movies_from_tmdb("movie/now_playing")
    upcoming = fetch_movies_from_tmdb("movie/upcoming")

    context = {
        "trending": preprocess_movies(trending.get("results", [])),
        "now_playing": preprocess_movies(now_playing.get("results", [])),
        "upcoming": preprocess_movies(upcoming.get("results", [])),
    }

    return render(request, "movies_app/home.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'movies_app/signup.html', {'form': form})

def watchlist_view(request):
    user_watchlist = Watchlist.objects.filter(user=request.user)
    return render(request, "movies_app/watchlist.html", {"watchlist": user_watchlist})

def add_to_watchlist(request):
    if request.method == "POST":
        movie_id = request.POST.get("movie_id")
        title = request.POST.get("title")
        poster_path = request.POST.get("poster_path")
        vote_average = request.POST.get("vote_average")

        Watchlist.objects.get_or_create(
            user=request.user,
            movie_id=movie_id,
            defaults={
                "title": title,
                "poster_path": poster_path,
                "vote_average": vote_average,
            }
        )
    return redirect("home")

def custom_logout(request):
    logout(request)
    return redirect('login')

