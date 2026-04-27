from django import forms
from movie_watchlist.models import Movie, Watchlist


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "release_year", "description", "genres"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "release_year": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "genres": forms.CheckboxSelectMultiple(),
        }


class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ["movie", "status", "rating"]
        widgets = {
            "movie": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 10}),
        }