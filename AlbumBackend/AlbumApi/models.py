from django.db import models


class Album(models.Model):
    title = models.CharField("Album Title", max_length=100)
    year_released = models.PositiveIntegerField()
    number_of_songs = models.PositiveIntegerField(blank=True)

    def save(self, *args, **kwargs):
        songs = self.songs.all()
        self.number_of_songs = len(songs)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField("Artist Name", max_length=100)
    date_of_birth = models.DateField()
    number_of_songs = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # If the object was created for the first time
        super(Artist, self).save(*args, **kwargs)
        self.number_of_songs = len(self.songs.all())
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField("Song Title", max_length=100)
    date_created = models.DateField()
    album = models.ForeignKey(
        Album, related_name="songs", on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist, related_name="songs")

    def save(self, *args, **kwargs):
        self.album.number_of_songs = len(self.album.songs.all())
        super(Song, self).save(*args, **kwargs)
        self.album.save()
        artists = self.artist.all()
        for artist in artists:
            artist.save()

    def __str__(self):
        return self.title
