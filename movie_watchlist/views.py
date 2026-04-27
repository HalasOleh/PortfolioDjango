from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods

from movie_watchlist.models import Movie, Genre, Watchlist
from movie_watchlist.forms import MovieForm

User = get_user_model()


@require_http_methods(["GET", "POST"])
def logout_view(request):
    auth_logout(request)
    return redirect("movie_watchlist:home")


def register(request):
    if request.user.is_authenticated:
        return redirect("movie_watchlist:home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Акаунт створено!")
            return redirect("movie_watchlist:home")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


def home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        watched_list = Watchlist.objects.filter(
            user=request.user, status="watched"
        )
    else:
        watched_list = Watchlist.objects.none()
    num_movies = Movie.objects.count()
    num_genres = Genre.objects.count()
    context = {
        "watched_list": watched_list,
        "num_movies": num_movies,
        "num_genres": num_genres,
    }
    return render(request, "movie_watchlist/home.html", context=context)


class MovieListView(generic.ListView):
    model = Movie
    template_name = "movie_watchlist/movie_list.html"

    def get_queryset(self):
        return Movie.objects.prefetch_related("genres")


class GenreListView(generic.ListView):
    model = Genre
    template_name = "movie_watchlist/genre_list.html"


@login_required
def dashboard(request):
    items = Watchlist.objects.filter(
        user=request.user
    ).select_related("movie")

    return render(request, "movie_watchlist/dashboard.html", {"items": items})


@login_required
def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            Watchlist.objects.get_or_create(
                user=request.user,
                movie=movie,
                defaults={"status": "plan"},
            )
            messages.success(request, "Фільм додано до вашого списку!")
            return redirect("movie_watchlist:movie_list")
    else:
        form = MovieForm()
    return render(request, "movie_watchlist/movie_form.html", {"form": form})


@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Фільм оновлено!")
            return redirect("movie_watchlist:movie_detail", pk=pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, "movie_watchlist/movie_form.html", {"form": form})


@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Фільм видалено!")
        return redirect("movie_watchlist:movie_list")
    return render(request, "movie_watchlist/movie_confirm_delete.html", {"movie": movie})


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "movie_watchlist/movie_detail.html"
