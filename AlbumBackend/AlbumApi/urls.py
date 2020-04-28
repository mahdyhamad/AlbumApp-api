from django.urls import path
from rest_framework import routers
from .views import ArtistViewSet, SongViewSet, AlbumViewSet

router = routers.DefaultRouter()
router.register('artists', ArtistViewSet, 'AlbumApi')
router.register('songs', SongViewSet, 'AlbumApi')
router.register('albums', AlbumViewSet, 'AlbumApi')

urlpatterns = router.urls