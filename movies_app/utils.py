from django.conf import settings
import requests

def fetch_movies_from_tmdb(endpoint):
    url = f"https://api.themoviedb.org/3/{endpoint}?language=en-US&page=1"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {settings.TMDB_BEARER_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("TMDb API Error:", e)
        return {"results": []}

def preprocess_movies(movies):
        for movie in movies:
            movie["display_title"] = movie.get("title") or movie.get("name") or "Untitled"
            movie["display_rating"] = movie.get("vote_average", "N/A")
        return movies
