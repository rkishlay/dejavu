from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Album(models.Model):
    """Create an album in music table."""
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=2000)

    def __str__(self):
        return self.album_title + ", Artist: " + self.artist


@python_2_unicode_compatible
class Song(models.Model):
    """Create a song linked with Album"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title + ", Album: " + self.album
