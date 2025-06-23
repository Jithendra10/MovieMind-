from django.db import models
from django.contrib.auth.models import User

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    release_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = ('user', 'movie_id')

    def __str__(self):
        return f"{self.title} ({self.movie_id})"

class LikedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Top1000Movie(models.Model):
    poster_link = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)
    released_year = models.IntegerField(null=True, blank=True)
    runtime = models.CharField(max_length=50, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    imdb_rating = models.FloatField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    star1 = models.CharField(max_length=255, null=True, blank=True)
    star2 = models.CharField(max_length=255, null=True, blank=True)
    star3 = models.CharField(max_length=255, null=True, blank=True)
    star4 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
