from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from movie_watchlist.models import Genre, Movie, Watchlist

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("pseudonym",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("pseudonym",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "pseudonym",)}),)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "release_year", "get_genres"]
    list_filter = ["genres", "release_year"]
    search_fields = ["title"]

    @admin.display(description="Genres")
    def get_genres(self, obj):
        return ", ".join(genre.name for genre in obj.genres.all())

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ["movie", "status"]
    list_filter = ["status"]
    search_fields = ["movie__title"]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
