from django.contrib import admin
from .models import Artist, Song, Album

# Register your models here
class SongInline(admin.TabularInline):
    model = Song
    fields = ["title", "date_created", "artist"]
    extra = 1

class ArtistInline(admin.TabularInline):
    model = Artist
    fields = ["name", "date_of_birth", "artist"]
    extra = 1



@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'date_of_birth')
    empty_value_display = '-empty-'

@admin.register(Song)
class ArtistAdmin(admin.ModelAdmin):
    list_display  = ('id', 'title', 'album')
    empty_value_display = '-empty-'
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year_released', 'number_of_songs')
    empty_value_display = '-empty-'
    inlines = [SongInline]
