from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('like/', views.like_movie, name='like_movie'),
    path('add-to-watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/', views.watchlist_view, name='watchlist'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='movies_app/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'), 
    path('liked/', views.liked_movies, name='liked_movies'),
]
