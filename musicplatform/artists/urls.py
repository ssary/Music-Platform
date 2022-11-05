
from django.urls import path
from .views import ArtistsView, ArtistView

urlpatterns = [
    path('', ArtistsView.as_view()),
    path('<int:id>/', ArtistView.as_view())
]