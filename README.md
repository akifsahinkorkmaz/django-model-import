# Django Model Import

When starting a new project, structuring data and logic is an important part of development. In Django structuring data is done with models. And logic part with urls, views, etc... Django models can have logic in them too.

The purpose of this project is showing what can go wrong when creating models in Django. And teaching system design skills to overcome this challenges. A music app will be created in this tutorial for demonstration purposes.

Frontend for music app is not a part of this tutorial.

## About Music App

The music app should have music, producers or listeners (users) and playlist at minimum complexity.

Music:
-   Music was produced by producers. Therefore music has producer(s). 
-   Music has a name.

Playlist:
-   Playlists are a collection for musics. Therefore playlist has music(s).
-   Playlist has a name.

User (producer or listener):
-   User can create playlist. User has a default playlist for musics they produced. Therefore user has playlist(s).
-   User has a name.

This structure (model) of data given above might not be the best solution out there for a music app. The data structure of the music app is modelled that way because it coincides with tutorial's purpose. 

## Setup

Setup a Django project with 3 additional django apps (music, user, playlist). 

---
- `music_app` is the Django project's name in this tutorial. 

- `source/music_app` is the path of Django project.

- See `Setup.md` for further information.
---

## Django Models (for music_app)

### Music:
In `music_app/music/models.py` create a music model as:
```python
from django.db import models

# Music (id (default), name, producer(s))

# import user (producer(s))
from user.models import User

# Music model
class Music(models.Model):
    name = models.CharField(max_length=200, verbose_name="music_name")
    producer = models.ManyToManyField(User)

    def __str__(self):
        return self.name
```

Register model in `music_app/music/admin.py` as:

```python
from django.contrib import admin
from .models import Music

# Register Music model
admin.site.register(Music)
```

### Playlist:
In `music_app/playlist/models.py` create a playlist model as:
```python
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
```

Register model in `music_app/playlist/admin.py` as:

```python
from django.contrib import admin
from .models import Playlist

# Register Playlist model
admin.site.register(Playlist)
```

### User:
In `music_app/user/models.py` create a user model as:
```python
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
```

Register model in `music_app/user/admin.py` as:

```python
from django.contrib import admin
from .models import User

# Register User model
admin.site.register(User)
```

### Make migrations:

- Make migrations and migrate.
- See `Setup.md` for further information.

## Error

There is an error. For further information see `Error.md`.
