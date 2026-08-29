from django.shortcuts import render
from rest_framework import viewsets,generics, permissions, status,filters
from .models import Artist,Album,Song,Playlist,Favorite 
from .serializers import ArtistSerializer,AlbumSerializer,SongSerializer,PlaylistSerializer,FavoriteSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.

class ArtistViewset(viewsets.ModelViewSet):
    queryset=Artist.objects.all()
    serializer_class=ArtistSerializer
class AlbumViewset(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer
class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'artist__name']
class PlaylistViewset(viewsets.ModelViewSet):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FavoriteViewset(viewsets.ModelViewSet):
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_favorite(request, song_id):
    try:
        favorite=Favorite.objects.get(user=request.user, song_id=song_id)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Favorite.DoesNotExist:
        return Response({'detail': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def check_favorite(request):
    song_ids=request.data.get('song_ids',[])
    favorited_ids=list(
        Favorite.objects.filter(
            user=request.user,
            song_id__in=song_ids
        ).values_list('song_id',flat=True)
    )
    return Response({'favorited_ids': favorited_ids})