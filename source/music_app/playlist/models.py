from django.db import models

# Playlist (id (default), name, music(s))

# no need to import music

# Playlist model
class Playlist(models.Model):
    name = models.CharField(max_length=200, verbose_name="playlist_name")
    # music can be null or blank
    music = models.ManyToManyField('music.Music', blank=True)

    def __str__(self):
        return self.name