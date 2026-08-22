from rest_framework import serializers
from .models import Artist, Album, Song, Playlist, Favorite

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist 
        fields = '__all__'
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album 
        fields = '__all__'
class SongSerializer(serializers.ModelSerializer):
    artist_name=serializers.CharField(source='artist.name', read_only=True)
    album_title=serializers.CharField(source='album.title', read_only=True)
    class Meta:
        model=Song 
        fields = [
            'id',
            'title',
            'artist',
            'artist_name',
            'album',
            'album_title',
            'audio_file',
            'duration_seconds',
            'track_number',
        ]
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Playlist 
        fields = '__all__'
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite 
        fields = '__all__'
