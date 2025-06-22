from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import path
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

def custom_logout(request):
    logout(request)
    return redirect('login')

