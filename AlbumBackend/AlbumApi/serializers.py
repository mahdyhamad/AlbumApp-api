from rest_framework import serializers
from .models import Artist, Song, Album

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'name'
        ]

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True, many=True)
    class Meta:
        model = Song
        fields = [
            'id',
            'title',
            'date_created',
            'album',
            'artist'
        ]

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Album
        fields = [
            'title',
            'year_released',
            'number_of_songs',
            'songs'
        ]

