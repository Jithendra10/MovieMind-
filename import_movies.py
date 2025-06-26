# import_movies.py

import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviemind.settings")  # Change 'your_project' to your project folder
django.setup()

from movies_app.models import Top1000Movie


def clean_int(value):
    try:
        return int(value.strip())
    except:
        return None

def clean_float(value):
    try:
        return float(value.strip())
    except:
        return None

def clean_string(value):
    if value:
        return value.strip()
    return None


with open("top_1000_movies.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        try:
            movie = Top1000Movie(
                poster_link=clean_string(row.get("Poster_Link")),
                title=clean_string(row.get("Title")),
                released_year=clean_int(row.get("Released_Year")),
                runtime=clean_string(row.get("Runtime")),
                genre=clean_string(row.get("Genre")),
                imdb_rating=clean_float(row.get("IMDB_Rating")),
                overview=clean_string(row.get("Overview")), 
                director=clean_string(row.get("Director")),
                star1=clean_string(row.get("Star1")),
                star2=clean_string(row.get("Star2")),
                star3=clean_string(row.get("Star3")),
                star4=clean_string(row.get("Star4")),
            )
            movie.save()
            count += 1
        except Exception as e:
            print(f"⚠️ Skipping row due to error: {e}")

print(f"✅ Done! Imported {count} movies.")
