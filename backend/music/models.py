from django.db import models
from django.conf import settings 

# Create your models here.

class Artist(models.Model):
    name= models.CharField(max_length=200)
    bio=models.TextField(blank=True)
    image= models.ImageField(upload_to='artists/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.name

class Album(models.Model):
    title= models.CharField(max_length=200)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE, related_name='albums')
    cover_image= models.ImageField(upload_to='albums/', blank=True, null=True)
    release_date=models.DateField(blank=True, null=True)
    def __str__ (self):
        return f'{self.title}-{self.artist.name}'

class Song(models.Model):
    title= models.CharField(max_length=200)
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    album=models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)
    audio_file=models.FileField(upload_to='songs/')
    duration_seconds=models.PositiveIntegerField(default=0)
    track_number=models.PositiveIntegerField(default=1)
    def __str__ (self):
        return self.title

class Playlist(models.Model):
    name=models.CharField(max_length=200)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='playlists')
    songs= models.ManyToManyField(Song, related_name='playlists', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.name

class Favorite(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    song= models.ForeignKey(Song, on_delete=models.CASCADE, related_name='favorited_by')
    created_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user','song')