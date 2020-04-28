import graphene
from graphene_django.types import DjangoObjectType
from .models import Album, Song, Artist


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class Songtype(DjangoObjectType):
    class Meta:
        model = Song


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class Query(graphene.ObjectType):
    all_albums = graphene.List(AlbumType)
    all_songs = graphene.List(Songtype)
    all_artists = graphene.List(ArtistType)

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()

    def resolve_all_songs(self, info, **kwargs):
        return Song.objects.prefetch_related('artist').all()

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()


schema = graphene.Schema(query=Query)
