from django.db import models

# Playlist (id (default), name, music(s))

# import music
from music.models import Music

# Playlist model
class Playlist(models.Model):
    name = models.CharField(max_length=200, verbose_name="playlist_name")
    music = models.ManyToManyField(Music)

    def __str__(self):
        return self.name