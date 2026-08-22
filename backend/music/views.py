from django.shortcuts import render
from rest_framework import viewsets
from .models import Artist,Album,Song,Playlist,Favorite
from .serializers import ArtistSerializer,AlbumSerializer,SongSerializer,PlaylistSerializer,FavoriteSerializer
from rest_framework import generics, permissions 
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import IsOwnerOrReadOnly
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
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FavoriteViewset(viewsets.ModelViewSet):
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]