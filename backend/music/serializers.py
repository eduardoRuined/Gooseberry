from rest_framework import serializers
from .models import Artist, Album, Song, Playlist, Favorite
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

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
    stream_url= serializers.SerializerMethodField()
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
            'stream_url',
            'duration_seconds',
            'track_number',
        ]
    def get_stream_url(self, obj):
        request=self.context.get('request')
        url=f'/api/songs/{obj.id}/stream/'
        return request.build_absolute_uri(url) if request else url
    
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Playlist 
        fields = '__all__'
        read_only_fields=['owner']
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite 
        fields = '__all__'
        read_only_fields=['user']
class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True,validators=[validate_password])
    class Meta:
        model=User
        fields=[
            'id',
            'username',
            'email',
            'password'
        ]
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
        )
        return user