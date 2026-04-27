from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movie_watchlist import views as movie_watchlist_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/logout/", movie_watchlist_views.logout_view, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("movie_watchlist/", include("movie_watchlist.urls", namespace="movie_watchlist")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
