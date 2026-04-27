from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    pseudonym = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_year = models.IntegerField()

    genres = models.ManyToManyField("Genre", related_name="movies"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-release_year"]

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Watchlist(models.Model):

    STATUS_CHOICES = [
        ("plan", "Планую переглянути"),
        ("watching", "Дивлюся"),
        ("watched", "Переглянуто"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="watchlist"
    )

    movie = models.ForeignKey(
        "Movie",
        on_delete=models.CASCADE,
        related_name="watchlist_entries"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="plan"
    )

    rating = models.IntegerField(null=True, blank=True)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_at"]
        unique_together = ("user", "movie")

    def __str__(self):
        return f"{self.user.username}: {self.movie.title} ({self.status})"