from django.db import models

# User (id (default), name, playlist(s))

# import playlist
from playlist.models import Playlist

# User model
class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="user_name")
    playlist = models.ManyToManyField(Playlist)

    def save(self, *args, **kwargs):
        # Save model before creating a default playlist
        super().save(*args, **kwargs)

        default_playlist = Playlist(name="%s's musics" %self.name)
        default_playlist.save()
        self.playlist.add(default_playlist)

    def __str__(self):
        return self.name