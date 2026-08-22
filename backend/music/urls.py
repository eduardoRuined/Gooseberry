from rest_framework.routers import DefaultRouter
from .views import ArtistViewset,AlbumViewset,SongViewset,PlaylistViewset,FavoriteViewset

router=DefaultRouter()
router.register(r'artists',ArtistViewset)
router.register(r'albums',AlbumViewset)
router.register(r'songs',SongViewset)
router.register(r'playlists',PlaylistViewset)
router.register(r'favorites',FavoriteViewset)

urlpatterns=router.urls
