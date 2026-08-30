from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Artist,Song, Playlist

# Create your tests here.

class SongApiTests(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpass123')
        self.artist= Artist.objects.create(name='Artista de Prueba')

    def test_list_songs_no_auth_required(self):
        response= self.client.get('/api/songs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_song_search_filters_correctly(self):
        Song.objects.create(
            title='Cancion Buscable',
            artist=self.artist,
            audio_file='songs/test.mp3'
        )
        Song.objects.create(
            title='Otra Diferente',
            artist=self.artist,
            audio_file='songs/test2.mp3'
        )
        response= self.client.get('/api/songs/',{'search':'Buscable'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Cancion Buscable')

class PlaylistAPITests(APITestCase):
    def setUp(self):
        self.user1=User.objects.create_user(username='user1', password='pass123')
        self.user2=User.objects.create_user(username='user2', password='pass123')
        self.playlist= Playlist.objects.create(name='Mi Playlist', owner=self.user1)

    def authenticate_as(self, user):
        token= RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_cannot_create_playlist_without_auth(self):
        response= self.client.post('/api/playlists/', {'name':'Nueva'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_owner_can_delete_own_playlist(self):
        self.authenticate_as(self.user1)
        response= self.client.delete(f'/api/playlists/{self.playlist.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_other_user_cannot_delete_playlist(self):
        self.authenticate_as(self.user2)
        response= self.client.delete(f'/api/playlists/{self.playlist.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)