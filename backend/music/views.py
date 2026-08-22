from django.shortcuts import render
from rest_framework import viewsets
from .models import Artist,Album,Song,Playlist,Favorite
from .serializers import ArtistSerializer,AlbumSerializer,SongSerializer,PlaylistSerializer,FavoriteSerializer

# Create your views here.

class ArtistViewset(viewsets.ModelViewSet):
    queryset=Artist.objects.all()
    serializer_class=ArtistSerializer
class AlbumViewset(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer
class SongViewset(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
class PlaylistViewset(viewsets.ModelViewSet):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer
class FavoriteViewset(viewsets.ModelViewSet):
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer