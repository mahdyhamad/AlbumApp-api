import graphene
from AlbumApi.schema import Query as album_query


class Query(album_query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
