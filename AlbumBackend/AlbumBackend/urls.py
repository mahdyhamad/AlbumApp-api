from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema))
    # path('api/', include('AlbumApi.urls')),
    # path('api-auth/', include("rest_framework.urls"))
]
