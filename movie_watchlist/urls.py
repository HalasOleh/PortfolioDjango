from django.urls import path
from movie_watchlist import views
from .views import home, MovieListView, GenreListView,MovieDetailView

app_name = "movie_watchlist"

urlpatterns = [
    path("", home, name="home"),
    path("movies/create/", views.movie_create, name="movie_create"),
    path("movies/<int:pk>/edit/", views.movie_edit, name="movie_edit"),
    path("movies/<int:pk>/delete/", views.movie_delete, name="movie_delete"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("movie-list/", MovieListView.as_view(), name="movie_list"),
    path("genre-list/", GenreListView.as_view(), name="genre_list"),


    path("register/", views.register, name="register"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
]


