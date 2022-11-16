from django.urls import path, include
from .views import SongAPIView, ArtistAPIView

urlpatterns = [
    path('songsAPI/', SongAPIView.as_view()),
    path('songsAPI/<str:pk>/', SongAPIView.as_view()),
    path('artistsAPI/', ArtistAPIView.as_view()),
    path('artistsAPI/<str:pk>/', ArtistAPIView.as_view())
]