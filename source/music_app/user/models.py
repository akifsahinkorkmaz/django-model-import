from django.db import models

# User (id (default), name, playlist(s))

# importing playlist is necessary
# Playlist class will be used on save method!
from playlist.models import Playlist

# User model
class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="user_name")
    # playlist can be null or blank. 
    playlist = models.ManyToManyField('playlist.Playlist', blank=True)


    def save(self, *args, **kwargs):
        # Save model before creating a default playlist
        super().save(*args, **kwargs)

        # If model is newly created
        try: 
            self.playlist.get(name="%s's musics" %self.name)
        except:
            default_playlist = Playlist(name="%s's musics" %self.name)
            default_playlist.save()
            self.playlist.add(default_playlist)

    def __str__(self):
        return self.name