from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ArtistViewset,AlbumViewset,SongViewset,PlaylistViewset,FavoriteViewset,remove_favorite,check_favorite
from .streaming import stream_song 

router=DefaultRouter()
router.register(r'artists',ArtistViewset)
router.register(r'albums',AlbumViewset)
router.register(r'songs',SongViewset)
router.register(r'playlists',PlaylistViewset)
router.register(r'favorites',FavoriteViewset)

urlpatterns=[ path('favorites/remove/<int:song_id>/', remove_favorite, name='remove-favorite'),
            path('favorites/check/',check_favorite,name='check-favorite'),
            path('songs/<int:song_id>/stream/',stream_song, name='stream-song'),
            ]+router.urls
